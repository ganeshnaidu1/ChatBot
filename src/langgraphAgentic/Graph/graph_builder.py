from langgraph.graph import StateGraph,START,END
from src.langgraphAgentic.State.GroqState import state
from src.langgraphAgentic.Nodes.GroqNode import BasicChatBotnode
from src.langgraphAgentic.Tools.Tavily import Tavily

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

    def basic_chatbot_build_graph_with_tavily(self,apiKey):
        """
        chat bot with tavily search
        """
        self.llm.bind_tools([Tavily])
        self.GroqNode=BasicChatBotnode(self.llm)
        self.graph_builder.add_node("chatbot",self.GroqNode.process)
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_edge("chatbot",END)

    def setupGraph(self,usecase,apiKey=None):
        if usecase=="Basic Chatbot":
            self.basic_chatbot_build_graph()
        elif usecase=="Chatbot with tool":
            self.basic_chatbot_build_graph_with_tavily(apiKey)

    def get_graph(self):
        return self.graph_builder