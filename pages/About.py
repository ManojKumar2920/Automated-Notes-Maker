import streamlit as st
from matplotlib import image
import os

st.set_page_config(page_title="Our Team", page_icon=":guardsman:", layout="wide")

# Define CSS style for centering text
centered_text = """
    <style>
        .centered {
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            height: 100%;
        }
    </style>
"""

# Add CSS styling to Streamlit app
st.markdown(centered_text, unsafe_allow_html=True)

# Define CSS style for buttons
button_style = """
    <style>
        .button {
            border-radius: 20px;
            border: none;
            color: white;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            transition-duration: 0.4s;
            cursor: pointer;
        }

        .button-blue {
            background-color: #0072b1;
        }

        .button-white {
            background-color: white;
            color: #0072b1;
        }

        .button-pink {
            background-color: #e1306c;
        }
    </style>
"""

# Add CSS styling to Streamlit app
st.markdown(button_style, unsafe_allow_html=True)

# Mano
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
dir_of_interest = os.path.join(PARENT_DIR, "resources")
IMAGE_PATH = os.path.join(dir_of_interest, "Mano.jpg")

img = image.imread(IMAGE_PATH)

col1, col2 = st.columns([1, 4])
with col1:
    st.image(img, width=150, caption='Manoj Kumar')

with col2:
    st.header('Manoj Kumar')

click = st.button('Know about Manoj', key='Manoj')
if click == True:
    st.write('Data Science Enthusiast')
    st.write('Follow and Connect with on these platforms !')
    
    url = 'https://www.linkedin.com/in/manojkumar20'
    st.markdown(f'''<a href={url} class="button button-blue">LinkedIn</a>''',unsafe_allow_html=True)
    
    url = 'https://github.com/ManojKumar2920'
    st.markdown(f'''<a href={url} class="button button-white">Github</a>''',unsafe_allow_html=True) 
    
    url = 'https://instagram.com/mano._29'
    st.markdown(f'''<a href={url} class="button button-pink">Instagram</a>''',unsafe_allow_html=True) 

# Janani
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
dir_of_interest = os.path.join(PARENT_DIR, "resources")
IMAGE_PATH = os.path.join(dir_of_interest, "Jana.jpeg")

img = image.imread(IMAGE_PATH)

col1, col2 = st.columns([1, 4])
with col1:
    st.image(img, width=150, caption='Janani')

with col2:
    st.header('Janani')

click2 = st.button('Know about Janani', key='Janani')
if click2 == True:
    st.write('Full Stack Enthusiast')
    st.write('Follow and Connect with on these platforms !
