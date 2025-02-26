import pandas as pd
import mysql.connector
from mysql.connector import Error

# 연료 타입 매핑 (친환경차 열은 제외)
FUEL_MAPPING = {
    "전기": "elec",
    "수소": "hydro",
    "하이브리드": "hybrid"
}

# 미리 정의된 지역 목록 (CSV의 행 순서대로 할당)
REGION_LIST = [
    "서울", "부산", "대구", "인천", "광주", "대전", "울산",
    "세종", "경기", "강원", "충북", "충남", "전북", "전남", "경북", "경남", "제주"
]

def populate_region_table(connection):
    """
    region 테이블에 REGION_LIST에 있는 지역들이 없다면 삽입합니다.
    """
    cursor = connection.cursor()
    cursor.execute("SELECT region_name FROM region;")
    existing = {row[0] for row in cursor.fetchall()}
    for region in REGION_LIST:
        if region not in existing:
            cursor.execute("INSERT INTO region (region_name) VALUES (%s)", (region,))
    connection.commit()
    cursor.close()

def get_region_mapping(connection):
    """
    DB의 region 테이블에서 region_name과 region_key의 매핑을 조회합니다.
    반환 예: {"서울": 1, "부산": 2, ...}
    """
    query = "SELECT region_key, region_name FROM region;"
    cursor = connection.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    return {row[1]: row[0] for row in rows}

def insert_regional_car_count(connection, region_key, fuel_type, car_count, car_count_date):
    """
    regional_car_count 테이블에 (region_key, fuel_type, car_count, car_count_date) 데이터를 삽입합니다.
    """
    query = """
        INSERT INTO regional_car_count (region_key, fuel_type, car_count, car_count_date)
        VALUES (%s, %s, %s, %s)
    """
    cursor = connection.cursor()
    try:
        cursor.execute(query, (region_key, fuel_type, car_count, car_count_date))
        connection.commit()
    except Error as e:
        print(f"데이터 삽입 에러: {e}")
        connection.rollback()
    finally:
        cursor.close()

def process_csv_and_insert(csv_file, connection):
    """
    CSV 파일을 읽어 '전기', '수소', '하이브리드' 열만 선택하고,
    각 행에 대해 REGION_LIST의 순서대로 지역 이름을 할당한 후,
    DB의 region 테이블에서 조회한 region_key를 사용해 regional_car_count 테이블에 삽입합니다.
    """
    # CSV 파일을 두 행의 헤더로 읽습니다. (누락된 값은 빈 문자열로 채움)
    # index_col=0: CSV의 첫 번째 열(행 번호)을 인덱스로 사용합니다.
    df = pd.read_csv(csv_file, header=[0, 1], index_col=0).fillna('')
    
    # CSV에 지역 정보가 없으므로, 행 순서대로 REGION_LIST의 지역명을 새 열로 삽입합니다.
    df.insert(0, ("region", "region"), [REGION_LIST[i-1] for i in df.index])
    
    # allowed_fuels: '전기', '수소', '하이브리드' 열만 선택 (친환경차는 제외)
    allowed_fuels = {"전기", "수소", "하이브리드"}
    data_df = df.loc[:, df.columns.get_level_values(1).isin(allowed_fuels)]
    data_df.insert(0, ("region", "region"), df[("region", "region")])
    
    # MultiIndex 열(연도, 연료)을 long format으로 변환합니다.
    # future_stack=True 옵션 사용 (dropna 인자는 제거)
    df_long = data_df.set_index(("region", "region")).stack(level=[0, 1], future_stack=True).reset_index()
    df_long.columns = ["region", "year", "fuel", "car_count"]
    
    # 천 단위 구분자(,) 제거 후 정수형 변환 (빈 문자열은 None 처리)
    def safe_convert(x):
        s = str(x).replace(",", "").strip()
        return int(s) if s != '' else None
    df_long["car_count"] = df_long["car_count"].apply(safe_convert)
    
    # 각 행의 연도 값으로 해당 연도의 12월 31일 날짜 생성
    df_long["car_count_date"] = df_long["year"].astype(str) + "-12-31"
    
    # 연료 타입 매핑 적용
    df_long["fuel_mapped"] = df_long["fuel"].map(FUEL_MAPPING).fillna('')
    
    # DB의 region 매핑 조회 (region_name → region_key)
    region_mapping = get_region_mapping(connection)
    
    for idx, row in df_long.iterrows():
        region_name = str(row["region"]).strip()
        fuel = str(row["fuel_mapped"]).strip()
        count = row["car_count"]
        date = row["car_count_date"]
        
        if fuel == '' or count is None:
            print(f"Skipping row {idx} due to missing data: {row.to_dict()}")
            continue
        
        if region_name not in region_mapping:
            print(f"Region '{region_name}' not found in DB. Skipping row {idx}.")
            continue
        
        reg_key = region_mapping[region_name]
        insert_regional_car_count(connection, reg_key, fuel, count, date)
        print(f"Inserted row: Region: {region_name}, Region Key: {reg_key}, Fuel: {fuel}, Count: {count}, Date: {date}")

if __name__ == "__main__":
    csv_file = "../../data/eco_car_registration.csv"  # CSV 파일 경로를 실제 경로로 수정하세요.
    
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="green_car",
        allow_local_infile=True
    )
    
    try:
        populate_region_table(connection)
        process_csv_and_insert(csv_file, connection)
    finally:
        connection.close()
