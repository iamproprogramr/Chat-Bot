import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gen_ai

load_dotenv()

st.set_page_config(
    page_title="Chat with Lumina",
    page_icon=":brain:",
    layout="centered",
)

GOOGLE_API_KEY = "put your api key"

gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-pro')

def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role

if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

st.title("🤖Lumina - By Muhammad Yousaf")

for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)

user_prompt = st.chat_input("Ask me...")
if user_prompt:
    st.chat_message("user").markdown(user_prompt)

    
    if "who are you" in user_prompt.lower() or "your name" in user_prompt.lower() or "what are you" in user_prompt.lower() or "tell me about you" in user_prompt.lower() or "who made you" in user_prompt.lower() or "hy" in user_prompt.lower() or "who is lumina" in user_prompt.lower() or "are you gemini" in user_prompt.lower():
        lumina_response_text = (
            "Hy I am Lumina, designed by Muhammad Yousaf. My backend is powered by the Gemini Pro model."
        )
    else:
        lumina_response = st.session_state.chat_session.send_message(user_prompt)
        lumina_response_text = lumina_response.text

    with st.chat_message("assistant", avatar='🤖'):
        st.markdown(lumina_response_text)
