import streamlit as st
from matplotlib import image
import os

# Define the CSS style for the buttons
button_style = """
    background-color: #008CBA;
    color: white;
    padding: 10px 20px;
    border-radius: 5px;
    font-size: 1em;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    margin: 4px 2px;
    transition-duration: 0.4s;
    cursor: pointer;
"""

# Define the CSS animation for the buttons
button_animation = """
    &:hover {
        background-color: white;
        color: #008CBA;
        box-shadow: 0px 0px 20px #008CBA;
    }
"""

# Define the path to the images
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
dir_of_interest = os.path.join(PARENT_DIR, "resources")
IMAGE_PATHS = {
    "Mano": os.path.join(dir_of_interest, "Mano.jpg"),
    "Janani": os.path.join(dir_of_interest, "Jana.jpeg"),
    "Siva": os.path.join(dir_of_interest, "Siva.jpg")
}

# Define the function to display the profile information
def show_profile(name, image_path, position, linkedin_url, github_url, instagram_url):
    img = image.imread(image_path)

    st.image(img, width=200)
    st.header(name)

    click = st.button(f"Know about {name}")
    if click == True:
        st.write(position)
        st.write("Follow and Connect with on these platforms!")

        st.markdown(f'<a href="{linkedin_url}" target="_blank" rel="noopener noreferrer"><button style="{button_style}{button_animation}">Linkedin</button></a>', unsafe_allow_html=True)
        st.markdown(f'<a href="{github_url}" target="_blank" rel="noopener noreferrer"><button style="{button_style}{button_animation}">Github</button></a>', unsafe_allow_html=True)
        st.markdown(f'<a href="{instagram_url}" target="_blank" rel="noopener noreferrer"><button style="{button_style}{button_animation}">Instagram</button></a>', unsafe_allow_html=True)

# Show the profiles
show_profile("Manoj Kumar", IMAGE_PATHS["Mano"], "Data Science Enthusiast", "https://www.linkedin.com/in/manojkumar20", "https://github.com/ManojKumar2920", "https://instagram.com/mano._29")
show_profile("Janani", IMAGE_PATHS["Janani"], "Full Stack Enthusiast", "https://www.linkedin.com/in/janani-p-7a791222a", "https://github.com/Jananikani", "https://www.instagram.com/janani_kanii/")
show_profile("Siva Subramanian", IMAGE_PATHS["Siva"], "Full Stack Enthusiast", "https://www.linkedin.com/in/siva-subramanian-86017022a", "https://github.com/G-Siva", "https://www.instagram.com/siva_subramanian_1909")
