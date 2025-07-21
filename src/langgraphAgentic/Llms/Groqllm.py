import os
import streamlit as st
from langchain_groq import ChatGroq

class GroqLLm:
    def __init__(self,user_controls_input):
        self.user_controls_input=user_controls_input
    
    def get_llm_model(self):
        try:
            groq_api_key= self.user_controls_input["APIKey"]
            selected_groq_model=self.user_controls_input["groqModelOption"]

            if groq_api_key=='' and os.environ["GROQ_API_KEY"]=='':
                st.error("Please enter GROQ Api key")

            llm=ChatGroq(api_key=groq_api_key,model=selected_groq_model)

        except Exception as e:
            raise ValueError(f"Error occured with exception: {e}")
        return llm