import streamlit as st
from matplotlib import image
import os

# CSS styling
st.markdown("""
<style>
    .btn {
        background-color: #E8F1F2;
        border-radius: 20px;
        border: none;
        color: #000000;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
    }
    .btn-linkedin {
        background-color: #0A66C2;
        color: #FFFFFF;
    }
    .btn-github {
        background-color: #FFFFFF;
        color: #000000;
    }
    .btn-instagram {
        background-color: #FCAF45;
        color: #FFFFFF;
    }
    .btn:hover {
        background-color: #DDE9EA;
    }
</style>
""", unsafe_allow_html=True)

# Mano

FILE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
dir_of_interest = os.path.join(PARENT_DIR, "resources")
IMAGE_PATH = os.path.join(dir_of_interest, "Mano.jpg")

img = image.imread(IMAGE_PATH)

st.image(img, width=200)

st.header('Manoj Kumar')

click = st.button('Know about Manoj', key='manoj')
if click:
    st.write('Data Science Enthusiast')
    st.write('Follow and Connect with on these platforms!')

    url = 'https://www.linkedin.com/in/manojkumar20'
    st.markdown(f'<a href="{url}" class="btn btn-linkedin">LinkedIn</a>', unsafe_allow_html=True)

    url = 'https://github.com/ManojKumar2920'
    st.markdown(f'<a href="{url}" class="btn btn-github">Github</a>', unsafe_allow_html=True)

    url = 'https://instagram.com/mano._29'
    st.markdown(f'<a href="{url}" class="btn btn-instagram">Instagram</a>', unsafe_allow_html=True)

# Janani

FILE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
dir_of_interest = os.path.join(PARENT_DIR, "resources")
IMAGE_PATH = os.path.join(dir_of_interest, "Jana.jpeg")

img = image.imread(IMAGE_PATH)

st.image(img, width=200)

st.header('Janani')

click2 = st.button('Know about Janani', key='janani')
if click2:
    st.write('Full Stack Enthusiast')
    st.write('Follow and Connect with on these platforms!')

    url = 'https://www.linkedin.com/in/janani-p-7a791222a'
    st.markdown(f'<a href="{url}" class="btn btn-linkedin">LinkedIn</a>', unsafe_allow_html=True)

    url = 'https://github.com/Jananikani'
    st.markdown(f'<a href="{url}" class="btn btn-github">Github</a>', unsafe_allow_html=True)

    url = 'https://www.instagram.com/janani_kanii/'
    st.markdown(f'<a href="{url}" class="btn btn-instagram">Instagram</a>', unsafe_allow_html=True)

# Siva


FILE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
dir_of_interest = os.path.join(PARENT_DIR, "resources")
IMAGE_PATH = os.path.join(dir_of_interest, "Siva.jpg")

img = image.imread(IMAGE_PATH)

st.image(img,width=200)

st.header('Siva Subramanian')

click3 = st.button('Know about Janani', key='siva')
if click3:
    st.write('Full Stack Enthusiast')
    st.write('Follow and Connect with on these platforms!')

    url = 'https://www.linkedin.com/in/janani-p-7a791222a'
    st.markdown(f'<a href="{url}" class="btn btn-linkedin">LinkedIn</a>', unsafe_allow_html=True)

    url = 'https://github.com/Jananikani'
    st.markdown(f'<a href="{url}" class="btn btn-github">Github</a>', unsafe_allow_html=True)

    url = 'https://www.instagram.com/janani_kanii/'
    st.markdown(f'<a href="{url}" class="btn btn-instagram">Instagram</a>', unsafe_allow_html=True)   
