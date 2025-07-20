import streamlit as st
from src.langgraphAgentic.Ui.Streamlit.loadUi import LoadStreamlit



def load_langgraph_agentic_ui():
    """
    Loads and runs the LangGraph AgenticAI application with Streamlit UI.
    This function initializes the UI, handles user input, configures the LLM model,
    sets up the graph based on the selected use case, and displays the output while 
    implementing exception handling for robustness.
    """
    ui=LoadStreamlit()
    user_input=ui.loadUi()

    if not user_input:
        st.error("Failed to load user input from the UI")
        return
    
    user_message=st.chat_input("Please enter your question")
    