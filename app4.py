import streamlit as st
import pandas as pd

# 웹 상호작용 버튼

def main() :
    df = pd.read_csv('data2/iris.csv')

    # 버튼 만들기, 누르면 데이터프레임 출력
    if st.button('데이터 보기') :
        st.write(df.head(3))

    # 응용) 버튼(이름 대문자) 생성
    # 버튼 누르면 species 컬럼의 값을 대문자로 변환 후 출력
    if st.button('대문자') :
        st.write(df['species'].str.upper().head(3))

    # 라디오 버튼 : 여러개 중에 하나를 선택 할 때 사용
    # petal_length 컬럼을 오름차순 정렬해서 화면에 보여주기
    my_order = ['오름차순', '내림차순']
    status = st.radio('정렬방법선택', my_order)
    if status == my_order[0] :
        # df.sort_values('petal_length')
        st.write(df.sort_values('petal_length'))
    elif status == my_order[1] :
        st.write(df.sort_values('petal_length', ascending=False))

    # 체크 박스 : 체크 / 체크해제
    if st.checkbox('헤드 5개 보기'):
        st.write(df.head())
    else :
        st.text('헤드를 숨겼습니다.')

    # 셀렉트 박스 : 여러개 고르기
    language = ['Python', 'C', 'Java', 'Go', 'PHP']
    my_choice = st.selectbox('좋아하는 언어 선택', language)
    if my_choice == language[0] :
        st.write("파이썬 선택")
    # 이후 생략

    # 멀티 셀렉트 : 여러개 중에서 여러개를 선택 (해시태그 비슷)
    st.multiselect('여러개 선택 가능', language)
    
    # 멀티셀렉트를 이용해서 특정 컬럼만 호출
    # 유저에게 iris df 컬럼 출력 후 유저가 선택한 컬럼만 보여주기
    columns_list = df.columns
    choice_list = st.multiselect('컬럼을 선택하세요', columns_list)
    st.write( df[choice_list] )

    # 슬라이더 : 숫자 조정하는데 주로 사용
    age = st.slider('나이', 1, 120, 30, 10) # 시작값, 끝값, 기본값, 스텝
    st.text('제가 선택한 나이는 {}입니다.'.format(age))

    # 익스펜더
    with st.expander('Hello') :
        st.text('변경')
        st.write(df)

if __name__ == '__main__' : 
    main()