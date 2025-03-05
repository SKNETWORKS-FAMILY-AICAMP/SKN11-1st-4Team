import mysql.connector as mysql
import pandas as pd
import re, sys
from streamlit import cli as strcli

def run_db_script(connection):
  """
  DB 초기 설정이 담긴 script (green_car.sql)를 실행시킴.
  """
  
  cursor = connection.cursor()
  
  with open('./green_car.sql', 'r') as f:
    sqlFile = f.read()
  f.close()
  
  commands = sqlFile.split(';')
  for command in commands:
    try:
      if command.strip() != '':
        cursor.execute(command)
    except Exception as e:
      print(f'Command skipped: {command}')
      print(e)

  # insert initial values into region table
  with open('./data/eco_car_registration.csv', 'r') as f:
    df = pd.read_csv(f)
  f.close()
  
  query = 'INSERT INTO region VALUES (%s, %s)'
  i = 1
  for region in df.iloc[2:19, :1].iloc[:, 0]:  # bad implementation; need extra preprocessing method to wrap this 
    cursor.execute(query, (i, region))
    i+=1
  
  connection.commit()
  cursor.close()
  return


def load_data_to_db(connection):
  """
  데이터들을 DB에 로드함.
  """
  from eco_car_DB import populate_region_table, process_csv_and_insert

  # 친환경자동차 data load
  
  eco_car_csv = './data/eco_car_registration.csv'
  populate_region_table(connection)
  process_csv_and_insert(eco_car_csv, connection)
  
  # TODO
  # 전체 자동차 등록 현황 data load

  # TODO
  # 충전소 현황 data load
  
  return

def render_streamlit():
  """
  streamlit을 실행함 - terminal이 아니라 python 내부에서 실행
  """
  
  sys.argv = ['streamlit', 'run', './streamlit/main_page.py']
  sys.exit(strcli.main())
  return



def main():
  connection = mysql.connect(
    host = 'localhost',
    user = 'root',
    password = '', # 실행하는 pc에 따라
    database = 'mysql'
  )

  run_db_script(connection)
  load_data_to_db(connection)
  render_streamlit_page()

  connection.close()
  

if __name__ == "__main__":
  main()
