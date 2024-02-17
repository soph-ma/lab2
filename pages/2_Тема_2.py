import streamlit as st
import pandas as pd
from PIL import Image

from footer import footer

st.page_link(label="Попередня тема:", page="pages/1_Тема_1.py")

st.title("ALFABET")

img1 = Image.open("/Users/sonic/Documents/coding/labs/lab2/pages/images/3.png")
st.image(img1)
st.markdown("<br><br>", unsafe_allow_html=True)

st.write("Proszę posłuchać i powtórzyć:")
st.video("https://www.youtube.com/watch?v=nvyQ980T_0k&pp=ygUh0L_QvtC70YzRgdGM0LrQuNC5INCw0LvRhNCw0LLRltGC")
st.markdown("<br><br>", unsafe_allow_html=True)

st.subheader("Наголос у польській мові")
st.write("Усім відомо, що в українській та російській мовах ми маємо плаваючий наголос. Та близькість  Польщі до германо-романських країн не обминула польську мову і тут. Ця близькість спростила вживання наголосу. Приблизно у 99,6% польських слів наголос падає на **передостанній склад**.")

st.markdown("---")
st.page_link(page="pages/3_Тема_3.py", label="Наступна тема")

st.markdown(footer, unsafe_allow_html=True)
