import streamlit as st
import pandas as pd

def run_eda() :
    st.subheader('EDA 화면')
    df = pd.read_csv('data2/iris.csv')
    # 컬럼을 선택하여 해당 컬럼만 보여주기
    choice = st.multiselect('컬럼 선택', df.columns)
    if len(choice) != 0 :
        st.write(df[choice])
        # 상관계수를 보여주기
        st.write(df[choice].corr())