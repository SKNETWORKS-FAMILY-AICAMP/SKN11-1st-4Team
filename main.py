import mysql.connect as mysql
import pandas as pd

def run_db_script():
  # run database script and insert initial values
  connection = mysql.connect(
    host = 'localhost',
    user = 'root',
    password = '', # 실행하는 pc에 따라
    database = 'mysql'
  )
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
  return


def load_databases():
  return

def render_streamlit():
  return

if __name__ == "__main__":
  run_db_script()
  load_databases()
  render_streamlit()

  exit()
