import streamlit as st
from PIL import Image

st.title('Bogdan')

VIDEO_URL = "https://www.youtube.com/watch?v=7pxqOmxPgPM"
st.video(VIDEO_URL)
st.write('Ritter')
img = Image.open('./Bogdan/Alexey-Savostin.jpg')
st.image(img)