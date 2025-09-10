import keys 
from langchain.chat_models import init_chat_model
import os
import streamlit as st

os.environ["GOOGLE_API_KEY"] = keys.GOOGLEKEY

model = init_chat_model("gemini-2.5-flash", model_provider="google_genai",
                         temperature = 0.7)

if 'text' not in st.session_state:
     st.session_state.text = ""

def clear_text():
     st.session_state.text = ""

st.title("Gemini Demo ")
prompt = st.text_area("Enter your prompt", key="text", height=100)
# Button to clear the text area
st.button("Clear All", on_click=clear_text)

if len(st.session_state.text) > 0 :
     response = model.invoke(prompt)
     st.write(response.content, unsafe_allow_html=True)

