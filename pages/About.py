import streamlit as st
from matplotlib import image
import os

# Define helper function to style button
def style_button(color):
    return f"""
        background-color: {color};
        border-radius: 5px;
        border: none;
        color: white;
        font-weight: bold;
        padding: 10px 20px;
    """

#Mano

FILE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
dir_of_interest = os.path.join(PARENT_DIR, "resources")
IMAGE_PATH = os.path.join(dir_of_interest, "Mano.jpg")

img = image.imread(IMAGE_PATH)

st.image(img, width=200, caption="Manoj Kumar")

st.write("&nbsp;")
st.write("&nbsp;")

st.write("**Data Science Enthusiast**")

st.write("&nbsp;")

st.write("Follow and connect with me on these platforms!")
st.write("&nbsp;")

url = 'https://www.linkedin.com/in/manojkumar20'
st.markdown(f'<a href="{url}"><button style="{style_button("lightblue")}">Linkedin</button></a>', unsafe_allow_html=True)

url = 'https://github.com/ManojKumar2920'
st.markdown(f'<a href="{url}"><button style="{style_button("white")}">Github</button></a>', unsafe_allow_html=True)

url = 'https://instagram.com/mano._29'
st.markdown(f'<a href="{url}"><button style="{style_button("lightpink")}">Instagram</button></a>', unsafe_allow_html=True)


#Janani

FILE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
dir_of_interest = os.path.join(PARENT_DIR, "resources")
IMAGE_PATH = os.path.join(dir_of_interest, "Jana.jpeg")

img = image.imread(IMAGE_PATH)

st.write("&nbsp;")
st.write("&nbsp;")

st.image(img, width=200, caption="Janani")

st.write("&nbsp;")
st.write("&nbsp;")

st.write("**Full Stack Enthusiast**")

st.write("&nbsp;")

st.write("Follow and connect with me on these platforms!")
st.write("&nbsp;")

url = 'https://www.linkedin.com/in/janani-p-7a791222a'
st.markdown(f'<a href="{url}"><button style="{style_button("lightblue")}">Linkedin</button></a>', unsafe_allow_html=True)

url = 'https://github.com/Jananikani'
st.markdown(f'<a href="{url}"><button style="{style_button("white")}">Github</button></a>', unsafe_allow_html=True)

url = 'https://www.instagram.com/janani_kanii/'
st.markdown(f'<a href="{url}"><button style="{style_button("lightpink")}">Instagram</button></a>', unsafe_allow_html=True)


#Siva

FILE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
dir_of_interest = os.path.join(PARENT_DIR, "resources")
IMAGE_PATH = os.path.join(dir_of_interest, "Siva.jpg")

img = image.imread(IMAGE_PATH)

st.write("&nbsp;")
st.write("&nbsp;")

st.image(img, width=200, caption="Siva Subramanian")

st.write("&nbsp;")
st.write("&nbsp;")

st.write("**Full Stack Enthusiast**")

st.write("&nbsp;")
