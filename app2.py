import streamlit as st
def main():
    st.title('타이틀 웹 대시보드')
    st.header('헤더 이 영역은 헤더')
    st.subheader('서브 헤더 이 영역은 서브헤더')
    st.text('텍스트 웹 대시보드 개발하기')
    st.success('작업이 성공 했을 때 사용하기')
    st.warning('경고 문구를 보여주고 싶을 때 사용하기')
    st.info('정보를 보여주고 싶을 때 사용하기')
    st.error('문제가 발생했을 때 사용하기')

    # 제 이름은 홍길동 입니다. 출력해보기
    name = '홍길동'
    st.text('제 이름은 {}입니다.'.format(name))

    # 파이썬의 함수 사용법을 보여주고 싶을 때
    st.help(sum)
    st.help(len)

if __name__ == '__main__' :
    main()
    

