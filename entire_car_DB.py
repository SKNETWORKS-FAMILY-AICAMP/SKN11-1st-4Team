import pandas as pd

df = pd.read_excel('./entire_region_cars_registration.xlsx')[3:]    # remove blank rows

# set multi-columns
column_tuples = []
for column in df.columns:
    t = df.loc[3:4, column].values
    column_tuples.append(tuple(t))

df.columns = pd.MultiIndex.from_tuples(column_tuples, names = ['car type', 'car usage'])
df = df.drop([3, 4])    # remove redundant rows

# set multi-index
index_tuples = []
for index in df.index:
    t = df.loc[index, ['월(Monthly)', '시도명', '시군구']].values
    index_tuples.append(tuple(t))

df.index = pd.MultiIndex.from_tuples(index_tuples, names = ['monthly', 'city', 'district'])

# get only sum-related data
df_sum_only = df.xs('계', level='district', axis=0) \
                .xs('계', level='car usage', axis=1)['총계']

# group by city
city_list = df_sum_only.index.get_level_values('city').unique()

for city in city_list:
    df_city = df_sum_only.xs(city, level='city')
    # group by year
    df_city.index = df_city.index.get_level_values('monthly').str.split('-').str[0] + '-12-31'
    df_city_sum_by_year = df_city.groupby('monthly')\
        .agg(lambda x: pd.to_numeric(x.str.replace(',', ''), errors='coerce').sum())
    
    # TODO: insert to DB after REGION_LIST is updated.
