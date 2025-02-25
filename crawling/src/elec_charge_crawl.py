from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import re
import time

# DRIVER_PATH = './chromedriver-linux64/chromedriver' # to be fixed - relative path

def get_elec_charge_info():
    
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless=new')

    # # !!!user-agent를 설정해줘야 될 필요가 있을 수도 있음!!!

    # service = webdriver.chrome.service.Service(DRIVER_PATH)
    # driver = webdriver.Chrome(service=service, options=options)

    driver =  webdriver.Chrome()

    url = 'https://chargeinfo.ksga.org/front/statistics/charger'
    driver.get(url)
    time.sleep(1)


    # 지역명 받아오기
    table = driver.find_element(By.CLASS_NAME, 'datatable')
    regions = table.find_elements(By.TAG_NAME, 'th')
    regions = [region.text for region in regions][1:]   # [0]: 연월 이므로 제거
    df = pd.DataFrame()

    tbody = table.find_element(By.TAG_NAME, 'tbody')
    div_by_year = tbody.find_elements(By.TAG_NAME, 'tr')

    for i in range(len(div_by_year)+1): # 연도별로 테이블을 나누기 위한 반복문
        single_row = tbody.find_elements(By.XPATH, f'//*[@id="tBodyList"]/tr[{i}]') # 한 줄 읽어오기

        for single_element in single_row:
            row = single_element.get_attribute('textContent')
            year = row[:4]
            row = row[4:]
            row = re.sub(r'\((.*?)\)', '\n', row)    # 괄호 안 % 나타내는 숫자 삭제
            row = [x for x in row.split('\n') if x.strip()]  # 빈 문자열 제거
            row_frame = pd.DataFrame({year: row}, index=regions)    # DataFrame으로 변환
            df = pd.concat([df, row_frame], axis=1)

    # print(df)
            
    driver.quit()
    return df


get_elec_charge_info()


"""
       2025     2024     2023     2022    2021    2020
서울   61,433   60,615   48,559   34,091  14,857   4,031
경기  117,039  112,384   77,364   50,587  22,892   7,597
인천   23,494   22,349   15,489    9,378   3,849   1,147
강원   14,317   13,818   10,515    6,424   3,164   1,634
충청   49,225   47,247   34,200   22,607  10,650   4,478
전라   39,746   38,585   27,044   17,870   9,880   4,836
경상   92,997   90,573   67,446   46,082  23,806   7,684
제주    8,408    8,561    7,531    5,909   4,943   3,307
합계  406,659  394,132  288,148  192,948  94,041  34,714


"""


