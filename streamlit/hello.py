import streamlit as st

st.title("Demo")
name = st.text_input("Enter your name", "Srikanth")
st.write(f"<h3>Hello {name}, welcome to the Streamlit Library! </h3>", 
          unsafe_allow_html=True )
     