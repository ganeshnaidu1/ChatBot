from langgraph.graph import StateGraph,START,END
from src.langgraphAgentic.State.GroqState import state
from src.langgraphAgentic.Nodes.GroqNode import BasicChatBotnode

class GraphBuilder:
    def __init__(self,model):
        self.llm=model
        self.graph_builder=StateGraph(state)

    def basic_chatbot_build_graph(self):
        """
        builds a basic chatbot using langgraph
        """
        self.GroqNode=BasicChatBotnode(self.llm)
        self.graph_builder.add_node("chatbot",self.GroqNode.process)
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_edge("chatbot",END)
        
    def setupGraph(self,usecase):
        if usecase=="Basic Chatbot":
            self.basic_chatbot_build_graph()

    def get_graph(self):
        return self.graph_builder