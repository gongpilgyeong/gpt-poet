import streamlit as st
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI

load_dotenv()
chat_model = ChatOpenAI()

st.title('GPT-시인')

content = st.text_input('시의 주제를 제시해주세요.')

if st.button('시 작성 요청'):
    with st.spinner('시 작성 중...'):
        result = chat_model.predict(content + "에 대한 시를 써줘")
        st.write(result)