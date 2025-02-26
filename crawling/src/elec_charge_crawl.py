import pandas as pd
pd.set_option('display.unicode.east_asian_width', True)

df = pd.read_excel('../files/elec_car_charges.xls', skiprows=3)

df_12 = df[df['년월'].str.endswith('-12')]

df_12 = df_12.rename(columns={'년월':'', '충전속도':''})
print(df_12)

