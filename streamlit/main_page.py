import streamlit as st

st.set_page_config(
    page_title="친환경 자동차 현황",
    layout="wide"
)

import pages.registration as registration
import pages.charging_map as charging_map
import pages.faq as faq
import pages.home as home


st.sidebar.title("📂 MENU")
menu = st.sidebar.radio(
    "페이지를 선택하세요:",
    ["🏠 Home", "📊 친환경 자동차 등록 현황", "💧 전국 충전소 설치 현황", "❓ FAQ"],
    key="main_menu"
)

st.markdown(
    """
    <style>
        [data-testid="stSidebarNav"] { display: none; }
    </style>
    """,
    unsafe_allow_html=True
)

if menu == "🏠 Home":
    home.run()
elif menu == "📊 친환경 자동차 등록 현황":
    registration.run()
elif menu == "💧 전국 충전소 설치 현황":
    charging_map.run()
elif menu == "❓ FAQ":
    faq.run()
