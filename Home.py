import streamlit as st

st.set_page_config(
    page_title='Automated Notes Maker',
    layout='wide',
    page_icon=':microphone:',
    initial_sidebar_state='expanded',
    # add CSS styles for background color
    page_bg_color="#f8f9fa",
    # set text color to black for better contrast
    text_color="black"
)

st.markdown(
    """
    <style>
    .title {
        font-size: 36px;
        color: #ff0000;
        text-align: center;
        margin-bottom: 50px;
    }
    .subtitle {
        font-size: 24px;
        color: #0000ff;
        text-align: center;
        margin-bottom: 30px;
    }
    .author {
        font-size: 18px;
        color: #808080;
        text-align: center;
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<p class="title">Automated Notes Maker</p>', unsafe_allow_html=True)

st.write('Automated notes maker from audio recordings is a tool used to covert the recordings of online classes and audio file to document notes . We build this using some Machine Learning algorithms to transcribe the spoken words into text and then create a summary or notes based on the transcribed text')

st.markdown('<p class="subtitle">Authors</p>', unsafe_allow_html=True)
st.markdown('<p class="author">Manoj Kumar</p>', unsafe_allow_html=True)
st.markdown('<p class="author">Janani</p>', unsafe_allow_html=True)
st.markdown('<p class="author">Siva Subramanian</p>', unsafe_allow_html=True)
