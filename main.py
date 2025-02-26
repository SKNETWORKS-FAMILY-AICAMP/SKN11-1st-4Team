import mysql.connect as mysql
import pandas as pd
import re, sys
from streamlit.web import cli as webcli

def run_db_script(connection):
  # run database script and insert initial values
  
  cursor = connection.cursor()
  
  with open('./green_car.sql', 'r') as f:
    sqlFile = f.read()
  f.close()
  
  commands = sqlFile.split(';')
  for command in commands:
    try:
      if command.strip() != '':
        cursor.execute(command)
    except Exception e:
      print(f'Command skipped: {command}')
      print(e)

  # insert initial values into region table
  with open('./data/eco_car_registration.csv', 'r') as f:
    df = pd.read_csv(f)
  f.close()
  
  query = 'INSERT INTO region VALUES (%s, %s)'
  i = 1
  for region in df.iloc[2:19, :1].iloc[:, 0]:  # bad
    cursor.execute(query, (i, region))
    i+=1
  
  connection.commit()
  cursor.close()
  return


def load_data_to_db(connection):
  from eco_car_DB import populate_region_table, process_csv_and_insert

  # 친환경자동차 data load into db
  
  eco_car_csv = './data/eco_car_registration.csv'
  populate_region_table(connection)
  process_csv_and_insert(eco_car_csv, connection)
  
  # 전체 자동차 data load

  # 충전소 data load
  
  return

def render_streamlit():
  sys.argv = ['streamlit', 'run', './streamlit/main_page.py']
  sys.exit(webcli.main())
  return

if __name__ == "__main__":
  connection = mysql.connect(
    host = 'localhost',
    user = 'root',
    password = '', # 실행하는 pc에 따라
    database = 'mysql'
  )
  
  run_db_script(connection)
  load_data_to_db(connection)
  render_streamlit()

