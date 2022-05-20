from base64 import encode
import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px

def main() :
    df= pd.read_csv('data2/lang_data.csv')
    st.write(df)

    lang_list = df.columns[ 1 : ]
    choice = st.multiselect('language', lang_list)
    if len(choice) != 0 :
        # 스트림릿에서 제공해주는 차트
        st.write(df[choice])
        st.line_chart(df[choice]) #(선)
        st.area_chart(df[choice]) #(영역)
        st.bar_chart(df[choice]) #(막대)
        st.header('스트림릿 차트 여기까지')

    # altair 차트
    df2 = pd.read_csv('data2/iris.csv')
    alt_chart = alt.Chart(df2).mark_circle().encode(x = 'petal_length', 
    y = 'petal_width', color = 'species')
    st.altair_chart(alt_chart)

    # streamlit 제공 map 차트
    df3 = pd.read_csv('data2/location.csv')
    st.write(df3)
    st.map(df3)


    # plotly 라이브러리를 이용한 차트 그리기 (스트림릿 제공)
    df4 = pd.read_csv('data2/prog_languages_data.csv')
    st.write(df4)

    # plotly의 pie차트, 원형
    fig1 = px.pie(df4, names='lang', values='Sum', title='각 언어별 파이차트')
    st.plotly_chart(fig1)
    # 플롯리 차트 전용 함수
    # 범계표의 데이터를 눌러 표기/미표기 설정

    # plotly의 bar차트, 막대
    df4_sorted = df4.sort_values('Sum', ascending=False)
    fig2 = px.bar(df4_sorted, x='lang', y='Sum')
    st.plotly_chart(fig2)

if __name__ == '__main__' :
    main()