import keys 
from langchain.chat_models import init_chat_model
import os
import streamlit as st

os.environ["GOOGLE_API_KEY"] = keys.GOOGLEKEY

model = init_chat_model("gemini-2.5-flash", 
                         model_provider="google_genai")
                         

st.title("Gemini Demo ")
prompt = st.text_area("Enter your prompt", height=100)

if len(prompt) > 0 :
     response = model.invoke(prompt)
     st.write(response.content, unsafe_allow_html=True)

