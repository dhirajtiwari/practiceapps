import streamlit as st
from streamlit_chat import message  # Import the message function from streamlit_chat
from dotenv import load_dotenv
import os

from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    SystemMessage, 
    HumanMessage,
    AIMessage
)

def init():
    load_dotenv()
    if os.getenv("OPEN_API_KEY") is None or os.getenv("OPEN_API_KEY") == "":
        print("open_api key is NOT set")
        exit(1)
    else:
        print("open api key is set, All is great")
    st.set_page_config(
        page_title="My first chat GPT App",
        page_icon=":-"
    )

def main():

    chat = ChatOpenAI(temperature=0.9)  

    messages = [
        SystemMessage(content="you are an assistant")
    ]


 # Use st.sidebar to create a sidebar in Streamlit
    with st.sidebar:
        user_input = st.text_input("Your message: ", key="user_input")

    st.header("My own chatGPT")

    if user_input:
            message(user_input, is_user=True)
            messages.append(HumanMessage(content=user_input))
            response = chat(messages)
            message(response.content, is_user=False)

    message("Hello, How are you? what is your name?")
    message("I am good, my name is VED", is_user=True)  # Use the message function to simulate chat messages
    
   

        
                            

if __name__ == "__main__":
    main()






