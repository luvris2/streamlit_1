import streamlit as st
import pandas as pd
import os
from datetime import datetime

def main() :
    # 1. 사이드바 만들기
    st.title('파일 업로드 프로젝트')
    
    menu = ['Image', 'CSV', 'About']
    choice = st.sidebar.selectbox('메뉴', menu)

    if choice == menu[0] :
        st.subheader('이미지 파일 업로드')
        upload_file = st.file_uploader('이미지 파일 선택', type=['jpg', 'png', 'jpeg'])
    
        if upload_file is not None :
            print(upload_file.name)
            print(upload_file.size)
            print(upload_file.type)
        
        # 파일명을 유니크하게 만들어서 저장해야 함
        # 현재시간을 활용해서 파일명 만들기
            current_time = datetime.now()
            current_time = current_time.isoformat().replace(':', '_')
            new_file_name = current_time + '.jpg'
            upload_file.name = new_file_name
            save_uploaded_file('temp', upload_file)
            
    elif choice == menu[1] :
        st.subheader('CSV 파일 업로드')
        upload_file = st.file_uploader('CSV 파일 선택', type=['CSV'])
        file_name_def(upload_file)

    else :
        st.subheader(' 파일 업로드 프로젝트 입니다')

# 디렉토리 정보와 파일을 알려주면, 해당 디렉토리에
# 파일을 저장하는 함수
def save_uploaded_file(directory, file) :
    # 1.디렉토리가 있는지 확인하여, 없으면 디렉토리부터만든다.
    if not os.path.exists(directory) :
        os.makedirs(directory)
    # 2. 디렉토리가 있으니, 파일을 저장.
    st.text(os.path.join(directory, file.name))
    with open(os.path.join(directory, file.name), 'wb') as f :
        f.write(file.getbuffer())
    return st.success("Saved file : {} in {}".format(file.name, directory))

# 현재 시간으로 파일명명 유니크화 함수
def file_name_def(upload_file) :
    if upload_file is not None :

        current_time = datetime.now()
        current_time = current_time.isoformat().replace(':', '_')
        new_file_name = current_time + '.jpg'
        upload_file.name = new_file_name
        save_uploaded_file('temp', upload_file)    

if __name__ == '__main__' :
    main()
