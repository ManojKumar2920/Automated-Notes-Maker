import streamlit as st
from matplotlib import image
import os

st.set_page_config(
    page_title='Automated Notes Maker',
    layout='wide',
    page_icon=':microphone:',
    initial_sidebar_state='expanded'
)

FILE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
dir_of_interest = os.path.join(PARENT_DIR, "resources")
IMAGE_PATH = os.path.join(dir_of_interest,"Cover.png")

img = image.imread(IMAGE_PATH)

st.image(img,width=200)

st.title(':red[Automated Notes Maker] :copyright:')

st.write('Automated notes maker from audio recordings is a tool used to covert the recordings of online classes and audio file to document notes . We build this using some Machine Learning algorithms to transcribe the spoken words into text and then create a summary or notes based on the transcribed text')

st.subheader('Authors')
st.write('Manoj Kumar')
st.write('Janani')
st.write('Siva Subramanian')

    
    
