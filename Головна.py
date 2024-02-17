import streamlit as st 
from footer import footer

welcome_text = f"""

Привіт. Тут ви зможете зробити перші кроки у вивченні польської мови.

**Доступні матеріали**:

"""
st.markdown(welcome_text)
st.page_link("pages/1_Тема_1.py")
st.page_link("pages/2_Тема_2.py")
st.page_link("pages/3_Тема_3.py")
st.page_link("pages/4_Тема_4.py")

st.write("**Тест для початківців**:")
st.page_link("pages/Тести.py")

st.markdown(footer, unsafe_allow_html=True)