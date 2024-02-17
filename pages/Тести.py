import streamlit as st 
import json
from footer import footer

st.title("Тестування за темами 1-4")

# Load questions from JSON file
with open("/mount/src/lab2/questions.json", "r") as f: 
    tasks = json.load(f)

# Initialize session state if it doesn't exist
if "current_question_index" not in st.session_state:
    st.session_state.current_question_index = 0

if "user_answers" not in st.session_state:
    st.session_state.user_answers = dict()

# Check if the test has started
if st.button("Розпочати тестування") or st.session_state.get("test_started", False):
    st.session_state.test_started = True

    current_question_index = st.session_state.current_question_index
    
    if current_question_index < len(tasks):
        # Get current question
        task = tasks[current_question_index]
        question = task["question"]
        correct_answer = task["correct"]
        options = task["options"]
        
        # Display question
        placeholder = st.empty()
        placeholder.write(question)
        
        # Get user answer
        user_answer = st.selectbox("Ваша відповідь:", options)

        if user_answer == correct_answer: 
            st.session_state.user_answers[current_question_index] = 2
            html_answer = "<span style='color:green'>Правильно</span>"
        elif user_answer != correct_answer: 
            st.session_state.user_answers[current_question_index] = 0
            html_answer = f"<span style='color:red'>Неправильно</span><br> <span>Правильна відповідь: {correct_answer}</span>"
            

        if st.button("Перевірити"): 
            st.markdown(html_answer, unsafe_allow_html=True)
        if st.button("Наступне запитання"):
            # Increment current question index
            st.session_state.current_question_index += 1
            # Force a rerun to reflect the updated question
            st.experimental_rerun()

    # Display score
    if "test_started" in st.session_state and st.session_state.current_question_index == len(tasks):
            score = sum(st.session_state.user_answers.values())
            st.subheader(f"Ваш результат: {score}/10")

# Footer
st.markdown(footer, unsafe_allow_html=True)
