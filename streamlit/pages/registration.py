import pymysql
import pandas as pd
import streamlit as st
# import plotly.express as px

eco_car_registration_csv = './data/eco_car_registration.csv'

def run():
    st.title("📊 등록 현황")

    # Markdown 문법으로 제목 및 서브 제목 꾸미기
    st.markdown("""
    <h3 style='color: #FF6347;'>지역별 및 연료별 등록 현황</h3>
    친환경 자동차의 최신 현황 데이터를 이용해 트렌드를 분석합니다.
    """, unsafe_allow_html=True)

    st.markdown("<h5 style='font-size: 16px;'>국내 지역별 / 연료별 자동차의 등록 결과를 확인할 수 있습니다.</h5>", unsafe_allow_html=True)

    # 텍스트 강조 및 정보 표시
    st.info("💡 **이 분석은 2024년 기준으로 지역별, 연료별 자동차 등록 현황을 시각화한 것입니다.**")

    df = pd.read_csv(eco_car_registration_csv)
    df = df.rename(index=lambda x: REGION_LIST[x-1])
    df = df.iloc[:, 2:]

    for col in df.columns[1:]:
        if df[col][0] == '전기':
            fig = px.bar(df, x=df.index, y=col, title=f'{col[:4]}년 전기 자동차 등록 현황')
            st.plotly_chart(fig)

        elif df[col][0] == '수소':
            fig = px.bar(df, x=df.index, y=col, title=f'{col[:4]}년 수소 자동차 등록 현황')
            st.plotly_chart(fig)

        elif df[col][0] == '하이브리드':
            fig = px.bar(df, x=df.index, y=col, title=f'{col[:4]}년 하이브리드 자동차 등록 현황')
            st.plotly_chart(fig)
