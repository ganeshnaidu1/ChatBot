import streamlit as st
from src.langgraphAgentic.Ui.Streamlit.loadUi import LoadStreamlit
from src.langgraphAgentic.Graph.graph_builder import GraphBuilder
from src.langgraphAgentic.Llms.Groqllm import GroqLLm
from src.langgraphAgentic.Ui.Streamlit.displayResult import DisplayResultStreamlit

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
    try:
        if user_message:
            obj_llm_config=GroqLLm(user_input)
            model=obj_llm_config.get_llm_model()
            if not model:
                st.error("LLm model cant be initialised")
            usecase=user_input.get("useCaseOptions")
            if not usecase:
                st.error("pick an use case")
            graph_builder=GraphBuilder(model=model)
            try:
                graph_builder.setupGraph(usecase)
                graph = graph_builder.get_graph()
                DisplayResultStreamlit(usecase,graph,user_message).display_result_on_ui()
            except:
                raise

    except Exception as e:
        raise

        
        
    