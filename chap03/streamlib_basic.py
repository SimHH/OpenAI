import streamlit as st
from openai import OpenAI
import random
import time
import os
from dotenv import load_dotenv

load_dotenv()

with st.sidebar:
    openai_api_key = os.getenv("OPENAI_API_KEY")

st.title("ChatBot")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Let's start chatting! 👇"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add tour OpenAI API Key to continue")
        st.stop()
    client = OpenAI(api_key = openai_api_key)
    st.session_state.messages.append({"role" : "user", "content" : prompt})
    st.chat_message("user").write(prompt)
    response = client.chat.completions.create(model="gpt-4o", messages=st.session_state.messages)
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role" : "assistant", "content" : msg})
    st.chat_message("assistant").write(msg) 