import streamlit as st
import os
from datetime import datetime

def main() :
    st.title('이미지 파일 업로드')
    upload_file = st.file_uploader('이미지 파일 선택', type=['jpg', 'png', 'jpeg'])
    # 이미지 업로더, 이미지 파일만 업로드하게 설정

    current_time = datetime.now()
    upload_file.name = current_time.isoformat().replace(':', '_') + '.jpg'
    # 지금 시간을 기준으로 업로드 파일 이름 설정

    with open(upload_file.name, 'wb') as f :
        f.write(upload_file.getbuffer())
        st.success("Saved file : {}".format(upload_file.name))
    # 파일 생성

if __name__ == '__main__' :
    main()
