import streamlit as st
import os
from src.langgraphAgentic.Ui.uicongigfile import Config

class LoadStreamlit:
    def __init__(self):
        self.config=Config()
        self.user_controls={}
    def loadUi(self):
        st.set_page_config(page_title= "🤖 " + self.config.getPageTitle(), layout="wide")
        st.header("🤖 " + self.config.getPageTitle())

        with st.sidebar:
            llm_options=self.config.get_llm_options()
            useCaseOptions=self.config.get_useCaseOptions()

            self.user_controls["selected_llm"]=st.selectbox("Select LLM",llm_options)

            if self.user_controls["selected_llm"]=="Groq":
                model_options=self.config.getGroqModelOptions()
                self.user_controls["groqModelOption"]=st.selectbox("Select Groq model",model_options)
                self.user_controls["APIKey"]=st.session_state["APIKey"]=st.text_input("APIKEY",type="password")
                
                if not self.user_controls["APIKey"]:
                    st.warning("Please enter the API Key")

            self.user_controls["useCaseOptions"]=st.selectbox("Select Use case",useCaseOptions)

        return self.user_controls
    
