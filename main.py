import argparse
import streamlit.web.cli as cli
import pandas as pd
import mysql.connector as mysql
from string import Template

def run_sql_script(connection, user_database_name):
    cursor = connection.cursor()

    with open('./eco_car.sql', 'r') as f:
        sql = f.read()

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

    # TODO: load entire car registration data to MYSQL


    # load eco car registration data to MYSQL
    from eco_car_DB import populate_region_table, process_csv_and_insert

    eco_car_csv = pd.read_csv('/data/eco_car_registration.csv')
    populate_region_table(connection)
    process_csv_and_insert(eco_car_csv, connection)

    # TODO: load eco car charging station data to MYSQL

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
        database=args.database_name
    )

    # load datas to created database
    load_data_to_db(connection)
    connection.close()

    # render pages using streamlit
    cli.main_run(['./streamlit/main_page.py', '--server.port', str(args.streamlit_port)])
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
