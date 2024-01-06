from dotenv import load_dotenv
load_dotenv() ## loading all the environment variables

## Import the required packages
import os
import streamlit as st
import google.generativeai as genai

## Store the environment key in .env file and configure it using genai
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Model to use of gemini ai
model = genai.GenerativeModel('gemini-pro')

## Initialise the chat state
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history = [])

## Display form title
st.title("Chat with Google Gemini-Pro!")

## Define the function to make relation between streamlit and geminiai
def role_to_streamlit(role):
    if role == "model":
        return "assistant"
    else:
        return role

## Print the message in the stored session
for message in st.session_state.chat.history:
    with st.chat_message(role_to_streamlit(message.role)):
        st.markdown(message.parts[0].text)

## Take the input from the user with the message written in the prompt box
if prompt := st.chat_input("I posses a well of knowledge. What would you like to know?"):
    st.chat_message("user").markdown(prompt)
    ## Send the message to the geminiai to get the response
    response = st.session_state.chat.send_message(prompt)
    ## Print the response from geminiai
    with st.chat_message("assistant"):
        st.markdown(response.text)