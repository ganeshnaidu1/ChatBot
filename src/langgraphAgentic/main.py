import streamlit as st
from src.langgraphAgentic.Ui.Streamlit.loadUi import LoadStreamlit
from src.langgraphAgentic.Graph.graph_builder import GraphBuilder
from src.langgraphAgentic.Llms.Groqllm import GroqLLm
from src.langgraphAgentic.Ui.Streamlit.displayResult import DisplayResultStreamlit
import os
import streamlit as st
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
        st.error("Error: Failed to load user input from the UI.")
        return

    # Initialize session state variable if not present
    if "IsFetchButtonClicked" not in st.session_state:
        st.session_state.IsFetchButtonClicked = False

    # Text input for user message
    if st.session_state.IsFetchButtonClicked:
        user_message = st.session_state.timeframe 
    else :
        user_message = st.chat_input("Enter your message:")

    if user_message:
            try:
                # Configure LLM
                obj_llm_config = GroqLLm(user_controls_input=user_input)
                model = obj_llm_config.get_llm_model()
                
                if not model:
                    st.error("Error: LLM model could not be initialized.")
                    return

                # Initialize and set up the graph based on use case
                usecase = user_input.get('useCaseOptions')
                if not usecase:
                    st.error("Error: No use case selected.")
                    return
                

                ### Graph Builder
                graph_builder=GraphBuilder(model)
                try:
                    print(usecase)
                    graph_builder.setupGraph(usecase)
                    graph = graph_builder.get_graph()
                    DisplayResultStreamlit(usecase,graph,user_message).display_result_on_ui()
                except Exception as e:
                    st.error(f"Error: Graph setup failed - {e}")
                    return
                

            except Exception as e:
                 raise ValueError(f"Error Occurred with Exception : {e}")

        
        
    