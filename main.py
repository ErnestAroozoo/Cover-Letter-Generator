import streamlit as st
import openai
import os
from dotenv import load_dotenv

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
load_dotenv()
openai.api_key = os.environ['OPENAI_API_KEY']

# Web App Layout
st.title("📝 Cover Letter Generator")
textbox = st.text_area("Input your resume here...")
textbox_button = st.button("Generate Cover Letter")
# Generate the cover letter
if textbox_button:
    prompt = f"Generate a cover letter for a job application based on the following information:\n{textbox}"
    completions = openai.Completion.create(engine="text-davinci-003", prompt=prompt, temperature=0.2, max_tokens=1024,
                                           top_p=0.9, frequency_penalty=1, presence_penalty=1, n=1, stop=None)
    cover_letter = completions.choices[0].text
    st.write(cover_letter)


