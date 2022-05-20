import streamlit as st
import pandas as pd
import os
from datetime import datetime

# app7의 응용, 여러 파일 업로드

def main() :
    st.title('여러 파일 한번에 업로드하는 앱')
    menu = ['Image', 'CSV', 'About']
    choice = st.sidebar.selectbox('메뉴', menu)

    if choice == menu[0] :
        st.subheader('이미지 파일 업로드')
        upload_file = st.file_uploader('이미지 파일 선택', type=['jpg', 'png', 'jpeg'], accept_multiple_files=True)
        for file in upload_file :
            file_name_def(file, 0)
            st.image(file)

    elif choice == menu[1] :
        st.subheader('CSV 파일 업로드')
        upload_file = st.file_uploader('이미지 파일 선택', type=['CSV'], accept_multiple_files=True)
        for file in upload_file :
            file_name_def(file, 1)   
            st.dataframe(pd.read_csv(file).head())

# 현재 시간으로 파일명명 유니크화 함수
def file_name_def(upload_file, ex) :
    if upload_file is not None :
        current_time = datetime.now()
        current_time = current_time.isoformat().replace(':', '_')
        if ex == 0 :
            new_file_name = current_time + '.jpg'
        elif ex == 1:
            new_file_name = current_time + '.csv'
        upload_file.name = new_file_name
        save_uploaded_file('temp', upload_file)    

# 파일 저장 함수
def save_uploaded_file(directory, file) :
    if not os.path.exists(directory) :
        os.makedirs(directory)
    st.text(os.path.join(directory, file.name))
    with open(os.path.join(directory, file.name), 'wb') as f :
        f.write(file.getbuffer())
    return st.success("Saved file : {} in {}".format(file.name, directory))

if __name__ == '__main__' :
    main()