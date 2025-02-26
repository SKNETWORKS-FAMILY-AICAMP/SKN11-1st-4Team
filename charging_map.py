import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pydeck as pdk
import pandas as pd
import streamlit as st
# from view.service.hyundai_analysis import render_brand_analysis, process_hyundai_data


def run():
    st.title("충전소 지도")

    data = pd.DataFrame([
    {"name": "충전소 A", "lat": 37.5665, "lon": 126.9780, "count": 5},
    {"name": "충전소 B", "lat": 37.5700, "lon": 126.9900, "count": 8},
    {"name": "충전소 C", "lat": 37.5600, "lon": 126.9700, "count": 3},
    ])

    # Pydeck Layer 설정
    layer = pdk.Layer(
        "ScatterplotLayer",
        data,
        get_position=["lon", "lat"],
        get_color=[0, 0, 255, 160],  # 파란색 계열
        get_radius="count * 100",  # 개수에 따라 크기 조절
        pickable=True,
    )

    # 지도 설정
    view_state = pdk.ViewState(
        latitude=37.5665,
        longitude=126.9780,
        zoom=12,
        pitch=0,
    )

    # Streamlit에 지도 표시
    st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state))