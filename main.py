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

# CUSTOMIZATION: Add custom footer
add_footer_style = """<style>
.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: #212121;
color: #f1f1f1;
text-align: center;
padding: 2px;
font-size: 12px;
}
a {
color: #f1f1f1;
text-decoration: none;
}
</style>
<div class="footer">
<p>Made by <a href='https://github.com/ErnestAroozoo' target='_blank'>Ernest Aroozoo</a> and <a href='https://github.com/rlaze' target='_blank'>Ryan Lazenby</a> | <a href='https://github.com/ErnestAroozoo/CoverLetterGenerator.net' target='_blank'>View on GitHub</a></p>
</div>
"""
st.markdown(add_footer_style, unsafe_allow_html=True)

# OpenAI API Key
load_dotenv()
openai.api_key = os.environ['OPENAI_API_KEY']

# Title
st.title("📝 Cover Letter Generator")
# Intro Text
intro = st.empty()
with intro.container():
    # Text body
    st.markdown("""
    ------------
    ### What is Cover Letter Generator?
    Cover Letter Generator is a web application that uses the power of OpenAI's GPT-3 model to generate custom cover letters for job applications. The app allows users to input their resume and then generates a cover letter tailored to the job they are applying for. The generated cover letter is based on the information provided by the user, making it unique and personalized. Cover Letter Generator is designed to make the job application process faster and more efficient by taking care of the tedious task of writing a cover letter.
    
    """)
    st.info(
        'Welcome to CoverLetterGenerator.net! To get started, please provide the required information below.',
        icon="ℹ️")
# User Inputs
user_name = st.text_input("Full Name:")
job_title = st.text_input("Job Title:")
company_name = st.text_input("Company Name:")
resume = st.text_area("Resume:")
generate_button = st.button("Generate Cover Letter", disabled=False)

# Generate the cover letter
if generate_button:
    with st.spinner("Please wait. Currently generating cover letter..."):
        prompt = f"Generate a cover letter for a job application as {job_title} at {company_name} for {user_name}.\nResume: {resume}"
        completions = openai.Completion.create(engine="text-davinci-003", prompt=prompt, temperature=0.2, max_tokens=1024,
                                               top_p=0.9, frequency_penalty=1, presence_penalty=1, n=1, stop=None)
        cover_letter = completions.choices[0].text
    st.write(cover_letter)

# CUSTOMIZATION: Change footer again to prevent clipping
add_footer_style2 = """<style>
.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: #212121;
color: #f1f1f1;
text-align: center;
padding: 2px;
font-size: 12px;
}
a {
color: #f1f1f1;
text-decoration: none;
}
</style>
<div class="footer">
<p>Made by <a href='https://github.com/ErnestAroozoo' target='_blank'>Ernest Aroozoo</a> | <a href='https://github.com/ErnestAroozoo/CoverLetterGenerator.net' target='_blank'>View on GitHub</a></p>
</div>
"""
st.markdown(add_footer_style2, unsafe_allow_html=True)
