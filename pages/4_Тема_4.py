import streamlit as st
import pandas as pd
from PIL import Image

from footer import footer

st.page_link(label="Попередня тема:", page="pages/3_Тема_3.py")

st.title("SKĄD JESTEŚ?")

img1 = Image.open("/Users/sonic/Documents/coding/labs/lab2/pages/images/4.png")
st.image(img1)

st.markdown("<br><br>", unsafe_allow_html=True)
st.subheader("Нові слова")
words_holder = st.container()
with words_holder: 
    st.write("co słychać? wszystko w porządku, wszystko dobrze, dlaczego, uczyć się polskiego, pracować, mój chłopak, moja dziewczyna, moje hobby, chcieć, bezokolicznik")
st.markdown("<br><br>", unsafe_allow_html=True)

st.write("Спробуйте перекласти діалоги:")
img2 = Image.open("/Users/sonic/Documents/coding/labs/lab2/pages/images/5.png")
st.image(img2)
st.markdown("<br><br>", unsafe_allow_html=True)

st.subheader("... І зовсім трохи граматики")

st.write("**Дієслово być**")
byc = {
    "Osoba" :["ja", "ty", "on/ona/ono", "my", "wy", "oni/one"],
    "Forma": ["jestem", "jesteś", "jest", "jesteśmy", "jesteście", "są"],
}
st.table(byc)

st.write("**One/oni**")
oneoni = """
    - on + on = oni 
    - on + ona = oni 
    - on + ono = oni

    - ona + ono = one 
    - ono + ono = one 
    - ona + ona = one

"""
st.write(oneoni)

st.markdown(footer, unsafe_allow_html=True)