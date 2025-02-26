import mysql.connect as mysql
import pandas as pd

# run database script
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


# insert region values
with open('./data/eco_car_registration.csv', 'r') as f:
  df = pd.read_csv(f)
f.close()

query = 'INSERT INTO region VALUES (%s, %s)'
i = 1
for region in df.iloc[2:19, :1].iloc[:, 0]:  # bad
  cursor.execute(query, (i, region))
  i+=1

connection.commit()


# load databases

# render streamlit
