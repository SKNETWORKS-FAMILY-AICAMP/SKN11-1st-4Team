import sys
import os
import csv
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
# from view.utils.data_refactoring import make_dataframe

def run():
    st.title("❓ 자주 묻는 질문 FAQ")
