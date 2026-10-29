import streamlit as st

faqs = {
    "library": "The library is open 9 AM to 5 PM, Monday to Saturday.",
    "canteen": "The canteen is open 8 AM to 4 PM.",
    "hackathon": "The internal hackathon is on 26 November 2026.",
}

st.title("Ask Campus")
q = st.text_input("Ask a question")

if q:
    answer = "Sorry, I don't know that yet."
    for keyword, reply in faqs.items():
        if keyword in q.lower():
            answer = reply
    st.write(answer)
