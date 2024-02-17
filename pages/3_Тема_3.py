import streamlit as st
import pandas as pd
from PIL import Image

from footer import footer

st.page_link(label="Попередня тема:", page="pages/2_Тема_2.py")

st.title("Przydatne rzeczy")

img1 = Image.open("/mount/src/lab2/pages/images/6.jpg")
st.image(img1)
st.markdown("<br><br>", unsafe_allow_html=True)

st.write("Прочитайте діалоги нижче вголос. Перекладіть незнайомі слова.")

st.subheader("Dialog 1")
st.write("""
         A. Przepraszam, gdzie jest toaleta? \n
         B. Toaleta jest tam, na prawo. \n
         A. Dziękuję bardzo.
         """)

st.subheader("Dialog 2")
st.write("""
         A. Przepraszam, gdzie jest Internet? \n
         B.Komputery są tutaj. Internet jest gratis. \n
         A. Dziękuję pani bardzo.
         """)

st.subheader("Dialog 3")
st.write("""
         A. Przepraszam, gdzie jest woda?\n
         B. Tu jest woda. Kawa, herbata i cukier są tam.\n
         A. Dziękuję.
         """)

st.subheader("Dialog 4")
st.write("""
         A. A co to jest?\n
         B. To jest program kulturalny. \n
         A. Program kulturalny? Co to jest? To coś specjalnego: film, spotkanie, specjalna lekcja.\n
         B. Aha, rozumiem.
         """)

st.markdown("---")
st.page_link(page="pages/4_Тема_4.py", label="Наступна тема")

st.markdown(footer, unsafe_allow_html=True)
