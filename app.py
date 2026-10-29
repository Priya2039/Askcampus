import streamlit as st st.title("ask campus")
q= st.text_input("ask a question")
if q:
st.write("you asked: "+q)
