import argparse
import streamlit.web.cli as cli
import pandas as pd
import mysql.connector as mysql
from string import Template

def run_sql_script(connection, user_database_name):
    cursor = connection.cursor()

    with open('./eco_car.sql', 'r') as f:
        sql = f.read()
    f.close()

    commands = sql.split(';')
    for command in commands:
        try:
            if 'CREATE DATABASE' in command or 'USE' in command: # replace database name
                command = Template(sql).substitute(
                    database_name = user_database_name
                )
            if command.strip() != '':
                cursor.execute(command)
        except Exception as e:
            print("Command skipped: ", command)
            print(e)

    connection.commit()
    cursor.close()


def load_data_to_db(connection):

    cursor = connection.cursor()

    # TODO: load entire car registration data to MYSQL - 배정수
    # 새로운 파이썬 파일을 만들어서
    # 해당 파일 안에서 전체 자동차 현황을 DB에 삽입해주세요
    # csv파일을 읽는 것도 여기서 하기 때문에
    # 함수를 작성할때에는 전처리가 안 된 csv 파일을 인자로 받았다고 가정하고 작성하면 됩니다.

    # load eco car registration data to MYSQL
    from eco_car_DB import populate_region_table, process_csv_and_insert

    eco_car_csv_dir = './data/eco_car_registration.csv'
    populate_region_table(connection)
    process_csv_and_insert(eco_car_csv_dir, connection)

    # TODO: load eco car charging station data to MYSQL - 정민호
    # 위와 동일하게 새로운 파이썬 파일을 만들어서
    # 해당 파일 안에서 충전소 현황을 DB에 삽입해주세요

    # TODO: load FAQ data to MYSQL

    connection.commit()
    cursor.close()


def main(args):
    # connect to MySQL
    init_connection = mysql.connect(
        host=args.host,
        user=args.user,
        password=args.password,
        database='mysql'
    )

    # create database using sql script
    run_sql_script(init_connection, args.database_name)
    init_connection.close()

    # connect to created database
    connection = mysql.connect(
        host=args.host,
        user=args.user,
        password=args.password,
        database=args.database_name,
        allow_local_infile=True,
    )

    # load datas to created database
    load_data_to_db(connection)
    connection.close()

    # render pages using streamlit
    cli.main_run(['./streamlit/main_page.py', '--streamlit.port', str(args.streamlit_port)])
    return


if __name__ == "__main__":
    # argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", type=str, default="localhost", help="MySQL host")
    parser.add_argument("--user", type=str, default="root", help="Username for MySQL host")
    parser.add_argument("--password", type=str, default="", help="Password for MySQL host")
    parser.add_argument("--database_name", type=str, default="eco_car", \
                        help="Database name that you want to use for this project")
    parser.add_argument("--streamlit_port", type=int, default=8501, help="Port number for Streamlit host")
    
    args = parser.parse_args()
    main(args)
