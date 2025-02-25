from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import re

DRIVER_PATH = './chromedriver-linux64/chromedriver' # to be fixed - relative path

def get_elec_car_info():
    
    options = webdriver.ChromeOptions()
    options.add_argument('--headless=new')

    # !!!user-agent를 설정해줘야 될 필요가 있을 수도 있음!!!

    service = webdriver.chrome.service.Service(DRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=options)

    url = 'https://chargeinfo.ksga.org/front/statistics/evCar'
    driver.get(url)

    # 지역명 받아오기
    table = driver.find_element(By.CLASS_NAME, 'datatable')
    regions = table.find_elements(By.TAG_NAME, 'th')
    regions = [region.text for region in regions][1:]   # [0]: 연월 이므로 제거
    df = pd.DataFrame()

    tbody = table.find_element(By.TAG_NAME, 'tbody')
    div_by_year = tbody.find_elements(By.TAG_NAME, 'tr')

    for i in range(len(div_by_year)): # 연도별로 테이블을 나누기 위한 반복문
        single_row = tbody.find_elements(By.XPATH, f'//*[@id="tBodyList"]/tr[{i}]') # 한 줄 읽어오기

        for single_element in single_row:
            row = single_element.get_attribute('textContent')
            year = row[:4]
            row = row[4:]
            row = re.sub(r'\((.*?)\)', '\n', row)    # 괄호 안 % 나타내는 숫자 삭제
            row = [x for x in row.split('\n') if x.strip()]  # 빈 문자열 제거
            row_frame = pd.DataFrame({year: row}, index=regions)    # DataFrame으로 변환
            df = pd.concat([df, row_frame], axis=1)
            
    driver.quit()
    return df

"""
       2024     2023     2022     2021     2020    2019    2018    2017    2016   2015   2014   2013 2012 2011
서울   79,548   72,937   59,327   40,564   23,393  14,952   9,564   4,797   1,498  1,151    785    475  205  103
부산   40,368   34,643   22,063   12,375    5,355   3,216   1,567     816     366    232    111     20   18    4
대구   32,631   30,396   24,161   16,185   12,630  11,313   6,605   2,005     344     88     22     12   11    7
인천   48,073   40,397   26,242   12,820    5,366   2,598   1,284     542     207    129    102     61   51   24
광주   13,820   12,538    9,096    5,194    3,210   2,464   1,447     548     239    186    111     24    5    2
대전   19,933   17,889   14,476    7,701    4,469   2,555   1,334     303      74     29     24     20   13    6
울산    8,883    7,838    5,061    3,166    2,274   1,447     847     356     103     54     18     12    9    7
세종    4,905    4,393    3,034    1,859    1,148     903     394      95      25     10      4      4    0    0
경기  134,741  114,117   77,648   39,958   20,477  11,750   6,383   2,290     650    313    169    108   84   39
강원   19,611   18,236   14,012    7,946    4,078   2,445   1,377     459     150     81     43     20   15   10
충북   22,759   19,972   15,140    8,194    3,883   2,412   1,199     281      60     28     16      8    5    1
충남   27,979   24,130   16,611    9,991    5,489   2,841   1,127     336     170    140    113     94   38    7
전북   22,494   19,795   12,727    7,365    3,323   1,841     997     336      57     37     18     13    8    2
전남   28,386   24,200   15,387    8,708    5,223   3,326   1,974     960     446    290    173     98   82   21
경북   30,810   26,776   19,154   11,240    7,051   4,051   2,001     756     278    147    111     62   49   13
경남   43,013   36,225   22,740   12,606    6,308   3,626   2,107   1,022     559    428    281    131   89   54
제주   43,117   39,418   32,976   25,571   21,285  18,178  15,549   9,206   5,629  2,369    674    302  178   44
계   621,071  543,900  389,855  231,443  134,962  89,918  55,756  25,108  10,855  5,712  2,775  1,464  860  344

이런식으로 나올겁니다.

df.iloc[0] = 0번째 row(=서울)를 쭉 출력해줍니다.
df.loc['부산'] = 부산 row를 쭉 출력해줍니다.
df.iloc[0]['2022'] = 서울 row의 2022년도 column을 출력해줍니다.

df['2024'] = 2024년 column을 쭉 출력해줍니다.

"""
