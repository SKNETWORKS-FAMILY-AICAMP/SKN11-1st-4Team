import streamlit as st
import pandas as pd
import plotly.express as px

def run():

    # CSV 파일 로드
    csv_file_path = "C:\\Users\\Playdata\\Desktop\\elec_car_chargers - Sheet1.csv"  # 실제 경로로 변경 필요
    df = pd.read_csv(csv_file_path, encoding="utf-8")

    # 올바른 헤더 설정 및 데이터 정리 (순서 조정)
    df = df.iloc[3:].reset_index(drop=True)
    df.columns = ["년월", "충전속도", "서울", "경기", "인천", "경상", "전라", "충청", "강원", "제주", "합계"]

    # 데이터 타입 변환 (숫자형 컬럼)
    numeric_cols = ["서울", "경기", "인천", "경상", "전라", "충청", "강원", "제주"]
    df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors="coerce")

    # 연도 및 월 추출 (헤더 설정 후 추출)
    df["연도"] = df["년월"].astype(str).str[:4]
    df["월"] = df["년월"].astype(str).str[5:7]

    # 연도-월별 데이터 저장
    year_month_data = {
        year: {
            month: df[(df["연도"] == year) & (df["월"] == month)].drop(columns=["합계"])
            for month in df[df["연도"] == year]["월"].unique()
        }
        for year in df["연도"].unique()
    }

    # 연도 선택
    selected_year = st.selectbox("연도를 선택하세요", sorted(year_month_data.keys(), reverse=True))
    selected_month = st.selectbox("월을 선택하세요", sorted(year_month_data[selected_year].keys(), reverse=True))
    df_filtered = year_month_data[selected_year][selected_month]

    # 막대그래프 생성
    fig = px.bar(
        df_filtered.melt(id_vars=["충전속도"], value_vars=numeric_cols),
        x="variable", y="value", color="충전속도",
        title=f"{selected_year}-{selected_month} 지역별 충전소 개수",
        labels={"variable": "지역", "value": "충전기 개수"}
    )
    st.plotly_chart(fig)
