#from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv,find_dotenv
import streamlit as st
from langchain_groq import ChatGroq

load_dotenv(find_dotenv())

model = ChatGroq(model="openai/gpt-oss-120b")#max_output_tokens=1000)


st.header('RESEARCH TOOLS')
user_input=st.text_input("Enter your query here")

if st.button('submit'):
    result=model.invoke(user_input)
    st.write(result.text)

