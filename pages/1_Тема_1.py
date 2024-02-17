import streamlit as st
import pandas as pd
from PIL import Image

from footer import footer

st.title("Pierwszy dzień w szkole")
st.markdown("<br><br>", unsafe_allow_html=True)

st.write("Спробуйте перекласти діалоги:")

img1 = Image.open("/mount/src/lab2/pages/images/1.png")
st.image(img1)
st.markdown("<br><br>", unsafe_allow_html=True)

st.subheader("Нові слова")
words_holder = st.container()
with words_holder: 
    st.write("tak, nie, proszę, dziękuję, przepraszam, nie rozumiem, nie wiem, proszę powtórzyć")
st.markdown("<br><br>", unsafe_allow_html=True)

st.subheader("Вітання в польській мові")
greetings = {
    'po polsku': ["Dzień dobry = добрий день", "Dobry wieczór = доброго вечора", "Witam = вітаю"],
    'po ukraińsku': ["Cześć = привіт", "Hej = привіт", "Siema = привіт (дуже неформально)"],
}
st.table(pd.DataFrame(greetings))
st.markdown("<br><br>", unsafe_allow_html=True)

st.write("Спробуйте здогадатися значення фраз в діалогах:")
img1 = Image.open("/mount/src/lab2/pages/images/2.png")
st.image(img1)
st.markdown("<br><br>", unsafe_allow_html=True)

st.write("Отже, запамʼятайте ще кілька додаткових фраз:")
phrases = {
    'po polsku': ["Dobranoc", "Do widzenia", "Do jutra", "Na razie", "Pa"],
    'po ukraińsku': ["На добраніч", "До побачення", "До завтра", "Бувай", "Бувай"],
}
st.table(phrases)



st.markdown("---")
st.page_link(page="pages/2_Тема_2.py", label="Наступна тема")

st.markdown(footer, unsafe_allow_html=True)