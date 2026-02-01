### Import Packages ########################################
import streamlit as st
from translator_main.translator_eurollm import translate_text

### Setup ###################################################
# Title of the app
st.set_page_config(page_title="Translator App", page_icon="🌍", layout="wide")

st.title('Translator App')


st.sidebar.subheader("About App")

st.sidebar.write("""
    This app allows users to translate text between multiple languages. The interface is simple and user-friendly, featuring the following components:
    
    **Instructions:**
    - Source Language Selection: Users can select the source language from a dropdown menu with options including English, German, French, and Spanish.
    - Target Language Selection: Users can select the target language from a similar dropdown menu.
    - Text Input Area: Users can enter the text they wish to translate in a text area.
    - A button labeled 'Submit' allows users to initiate the translation process.
""")




with st.form(key='my_form'):
    st.header("Translate Text:")
    source_lang = st.selectbox(label = "Source language:", options = ["English","German", "French", "Spanish"])
    target_lang = st.selectbox(label = "Target language:", options = ["English", "German", "French", "Spanish"])
    input_text = st.text_area("Enter the text to translate:")
    # Submit button
    submit_button = st.form_submit_button(label='Submit')
if submit_button:
    output = translate_text(source_lang, target_lang, input_text)
    st.info(output)

st.write("""Built by [Chaitanya Madduri](https://www.linkedin.com/in/v-s-chaitanya-madduri-2886447a/). Powered by Python 🐍 + EuroLLM+ + Streamlit 🎈""")