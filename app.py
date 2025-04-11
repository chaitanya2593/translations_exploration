### Import Packages ########################################
import streamlit as st
from translator_main.translator_eurollm import translate_text, question_text
### Setup ###################################################
# Title of the app
st.set_page_config(page_title="Translator App", page_icon="🌍", layout="wide")

st.title('Translator App')

# Sidebar for navigation
if st.sidebar.button("Translate"):
    page = "Translate"
elif st.sidebar.button("Translation Info"):
    page = "Translation Info"
else:
    page = "Translation Info"  # Default page

if page == "Translate":
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

elif page == "Translation Info":
    st.sidebar.write("""
        This app allows users to query thorugh the model and get the response. The interface is simple and user-friendly, featuring the following components:
        
        **Instructions:**
        - Only one request can be made at a time.
        - The app will display the answer from the model.
    """)
    st.header("Chat for Research Content")
    # Add new options here
    prompt = st.chat_input("Say something")
    USER = "user"
    ASSISTANT = "assistant"
    if prompt:
        print(prompt)
        st.chat_message(USER).write(prompt)
        ans = question_text(prompt)
        st.chat_message(ASSISTANT).write(ans)

    # # Display chat messages from history on app rerun
    # for message in st.session_state.messages:
    #     with st.chat_message(message["role"]):
    #         st.markdown(message["content"])
    #
    # # Accept user input
    # if prompt := st.chat_input("What is up?"):
    #     # Add user message to chat history
    #     st.session_state.messages.append({"role": "user", "content": prompt})
    #     # Display user message in chat message container
    #     with st.chat_message("user"):
    #         st.markdown(prompt)
    #
    #     # Display assistant response in chat message container
    #     with st.chat_message("assistant"):
    #         response = st.write_stream(question_text(input))
    #     # Add assistant response to chat history
    #     st.session_state.messages.append({"role": "assistant", "content": response})


st.write("""Built with ❤️ by [Chaitanya Madduri](https://www.linkedin.com/in/v-s-chaitanya-madduri-2886447a/). Powered by Python 🐍 + EuroLLM+ + Streamlit 🎈""")