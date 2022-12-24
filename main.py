import streamlit as st
import openai

# CUSTOMIZATION: Page configuration
st.set_page_config(
    page_title="Cover Letter Generator",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="expanded",
)

# CUSTOMIZATION: Hide unnecessary UI elements
hide_streamlit_style = """
                <style>
                div[data-testid="stToolbar"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                div[data-testid="stDecoration"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                div[data-testid="stStatusWidget"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                #MainMenu {
                visibility: hidden;
                height: 0%;
                }
                header {
                visibility: hidden;
                height: 0%;
                }
                footer {
                visibility: hidden;
                height: 0%;
                }
                .css-15zrgzn {display: none}
                #root > div:nth-child(1) > div > div > div > div > section > div {padding-top: 0rem;}
                </style>
                """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# OpenAI API Key
openai.api_key = "OPENAI_API_KEY"

# Web App Layout
st.title("📝 Cover Letter Generator")
textbox = st.text_area("Input your resume here...")
textbox_button = st.button("Generate Cover Letter")
if textbox_button:
    st.write(textbox)


