import streamlit as st
from diabetes_data import qa_pairs
from rapidfuzz import process

def find_best_answer(user_input):
    user_input = user_input.lower()
    questions = list(qa_pairs.keys())
    best_match, score, _ = process.extractOne(user_input, questions)
    if score > 70:
        return qa_pairs[best_match]
    else:
        return "معذرت، میں آپ کے سوال کو نہیں سمجھ سکا۔ براہ کرم دوبارہ کوشش کریں۔\nSorry, I couldn't understand your question. Please try rephrasing."

st.set_page_config(page_title="Diabetes Chatbot", layout="centered")
st.title("🩺 Diabetes Information Chatbot")
st.markdown("**Ask anything related to Diabetes in Urdu or English.**")

user_input = st.text_input("Type your question here (Urdu/English):")

if user_input:
    answer = find_best_answer(user_input)
    st.markdown("---")
    st.markdown(f"**Answer:**\n\n{answer}")
