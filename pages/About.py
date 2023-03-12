import streamlit as st
from matplotlib import image
import os

#Mano

FILE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
dir_of_interest = os.path.join(PARENT_DIR, "resources")
IMAGE_PATH = os.path.join(dir_of_interest, "Mano.jpg")

img = image.imread(IMAGE_PATH)

st.image(img,width=200)

st.header('Manoj Kumar')

click = st.button('Know about Manoj')
if click == True:
    st.write('Data Science Enthusiast')
    st.write('Follow and Connect with on these platforms !')
    

    url = 'https://www.linkedin.com/in/manojkumar20'
    st.markdown(f'''<a href={url}><button style="background-color:lightblue;">Linkedin</button></a>''',unsafe_allow_html=True)
    
    url = 'https://github.com/ManojKumar2920'
    st.markdown(f'''<a href={url}><button style="background-color:white;">Github</button></a>''',unsafe_allow_html=True) 
    
    url = 'https://instagram.com/mano._29'
    st.markdown(f'''<a href={url}><button style="background-color:lightpink;">Instagram</button></a>''',unsafe_allow_html=True) 
    

#Janani

FILE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
dir_of_interest = os.path.join(PARENT_DIR, "resources")
IMAGE_PATH = os.path.join(dir_of_interest, "Jana.jpeg")

img = image.imread(IMAGE_PATH)

st.image(img,width=200)

st.header('Janani')

click2 = st.button('Know about Janani')
if click2 == True:
    st.write('Full Stack Enthusiast')
    st.write('Follow and Connect with on these platforms !')
    

    url = 'https://www.linkedin.com/in/janani-p-7a791222a'
    st.markdown(f'''<a href={url}><button style="background-color:lightblue;">Linkedin</button></a>''',unsafe_allow_html=True)
    
    url = 'https://github.com/Jananikani'
    st.markdown(f'''<a href={url}><button style="background-color:white;">Github</button></a>''',unsafe_allow_html=True) 
    
    url = 'https://www.instagram.com/janani_kanii/'
    st.markdown(f'''<a href={url}><button style="background-color:lightpink;">Instagram</button></a>''',unsafe_allow_html=True) 
    

#Siva

FILE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
dir_of_interest = os.path.join(PARENT_DIR, "resources")
IMAGE_PATH = os.path.join(dir_of_interest, "Siva.jpg")

img = image.imread(IMAGE_PATH)

st.image(img,width=200)

st.header('Siva Subramanian')

click3 = st.button('Know about Siva')
if click3 == True:
    st.write('Full Stack Enthusiast')
    st.write('Follow and Connect with on these platforms !')
    

    url = 'https://www.linkedin.com/in/siva-subramanian-86017022a'
    st.markdown(f'''<a href={url}><button style="background-color:lightblue;">Linkedin</button></a>''',unsafe_allow_html=True)
    
    url = 'https://github.com/G-Siva'
    st.markdown(f'''<a href={url}><button style="background-color:white;">Github</button></a>''',unsafe_allow_html=True) 
    
    url = 'https://www.instagram.com/siva_subramanian_1909'
    st.markdown(f'''<a href={url}><button style="background-color:lightpink;">Instagram</button></a>''',unsafe_allow_html=True) 
