import streamlit as st
from matplotlib import image
import os

st.set_page_config(
    page_title='Automated Notes Maker',
    layout='wide',
    page_icon=':microphone:',
    initial_sidebar_state='expanded'
)

# Define CSS styles
css_styles = """
<style>
h1 {
    color: #FF0000;
    text-align: center;
    font-size: 50px;
    margin-top: 50px;
}
h2 {
    color: #008080;
    text-align: center;
    font-size: 30px;
    margin-top: 30px;
}
p {
    font-size: 20px;
    text-align: justify;
    margin: 20px 0;
}
</style>
"""

# Render CSS styles
st.markdown(css_styles, unsafe_allow_html=True)

# Render content with CSS styles applied
st.title('Automated Notes Maker')
st.header('Authors')
st.write('Manoj Kumar')
st.write('Janani')
st.write('Siva Subramanian')
st.write('Automated notes maker from audio recordings is a tool used to covert the recordings of online classes and audio file to document notes. We build this using some Machine Learning algorithms to transcribe the spoken words into text and then create a summary or notes based on the transcribed text.')
