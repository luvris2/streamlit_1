import streamlit as st
import pandas as pd
from PIL import Image
# 이미지 처리를 위한 라이브러리

# 웹에서 컨텐츠 표시

def main() :
    # 1. 저장되어 있는 이미지 파일 화면에 표시
    img = Image.open('data2/image_03.jpg')
    st.image(img)
    st.image(img, use_column_width = True)

    # 2. 인터넷 경로상의 이미지 화면에 표시
    img_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcREsOno1mhECt5tCEQ6HwudB--ygkbxMHw8Fy6048xSMOP_nhYcJWLLOJ0O6H9FzPIGWfU&usqp=CAU'
    st.image(img_url)

    # 3. 영상 화면에 표시
    video_file = open('data2\secret_of_success.mp4', 'rb')
    st.video(video_file)

    # 4. 오디오 화면에 표시
    audio_file = open('data2/song.mp3', 'rb')
    st.audio(audio_file.read(), format='audio/mp3')

if __name__ == '__main__' : 
    main()