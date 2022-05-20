import streamlit as st
import pandas as pd
import os
from datetime import datetime
import app9_home
import app9_EDA
import app9_ml
import app9_about

def main() :
    st.title(' 파일 분리 앱 ')
    menu = ['Home', 'EDA', 'ML', 'About']
    choice = st.sidebar.selectbox('메뉴', menu)

    if choice == menu[0] :
        app9_home.run_home()
    elif choice == menu[1] :
        app9_EDA.run_eda()
    elif choice == menu[2] :
        app9_ml.run_ml()
    elif choice == menu[3] :
        app9_about.run_about()

if __name__ == '__main__' :
    main()