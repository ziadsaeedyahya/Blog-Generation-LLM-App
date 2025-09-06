import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv 

# Configure Gemini API
load_dotenv()
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


## Function To get response from Gemini Flash
def getGeminiResponse(input_text, no_words, blog_style):
    # Load Gemini Flash Model
    model = genai.GenerativeModel("gemini-1.5-flash")

    # Prompt Template
    template = f"""
    Write a blog for {blog_style} job profile
    about the topic: "{input_text}"
    within {no_words} words.
    """

    # Generate Response
    response = model.generate_content(template)
    return response.text


# ---------------- Streamlit App ----------------
st.set_page_config(page_title="Generate Blogs",
                   page_icon='🤖',
                   layout='centered',
                   initial_sidebar_state='collapsed')

st.header("Generate Blogs 🤖")

input_text = st.text_input("Enter the Blog Topic")

## creating two more columns for additional fields
col1, col2 = st.columns([5,5])

with col1:
    no_words = st.text_input('No of Words')
with col2:
    blog_style = st.selectbox('Writing the blog for',
                              ('Researchers','Data Scientist','Common People'),
                              index=0)

submit = st.button("Generate")

## Final response
if submit:
    st.write(getGeminiResponse(input_text, no_words, blog_style))
