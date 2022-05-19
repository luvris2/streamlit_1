import streamlit as st
import pandas as pd

# 웹에서 컨텐츠 표시

def main() :
    # 1. 저장되어 있는 이미지 파일 화면에 표시
    st.image('data2/image_03.jpg')
    st.image('data2/image_03.jpg', use_column_width = True)

    # 2. 인터넷 경로상의 이미지 화면에 표시
    img_url = 'https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FVF9W6%2FbtrCCFKYs6k%2FxMJQ2AfBtZRiEJlML71Lak%2Fimg.png'
    st.image(img_url)

    # 3. 영상 화면에 표시
    video_file = open('data2\secret_of_success.mp4', 'rb')
    st.video(video_file)

    # 4. 오디오 화면에 표시
    audio_file = open('data2/song.mp3', 'rb')
    st.audio(audio_file.read(), format='audio/mp3')

if __name__ == '__main__' : 
    main()