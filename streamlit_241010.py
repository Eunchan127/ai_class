# Streamlit 라이브러리
#   데이터 분석에 특화되어 있고, 웹에 대한 기반 지식이 없어도 손쉽게 데이터 웹 대시보드를 제작할 수 있는 라이브러리

# title, header, subheader
import streamlit as st

st.title('This is title')
st.header('This is header')
st.subheader('This is subheader')


# markdown
st.markdown(
    '''
    This is main text.
    This is how to change the color of text :red[Red,] :blue[Blue,] :green[Green.]
    This is **Bold** and *Italic* text
    '''
)

# text
st.text(
    '''
    This is main text.
    This is how to change the color of text :red[Red,] :blue[Blue,] :green[Green.]
    This is **Bold** and *Italic* text
    '''
)


st.title('Title 1')
st.text('Text body 1')

st.divider()

st.title('Title 2')
st.text('Text body 2')

# ctrl + c : 터미널 종료 / 맥은 command + c
# 수정한걸 이어가고 싶으면 저장 후 페이지에서 새로고침
# 실행할 때 Terminal이 어느 파일에 열려있는지 확인
# cd ./ x : x파일로 들어가기
# cd ../ x : x파일 뒤로 돌아가기