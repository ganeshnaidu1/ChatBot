from langgraph.graph import StateGraph,START,END
from src.langgraphAgentic.State.GroqState import state
from src.langgraphAgentic.Nodes.GroqNode import BasicChatBotnode
from langgraph.prebuilt import tools_condition
from src.langgraphAgentic.Nodes.chat_bot_with_Toolnode import ChatbotWithToolNode
from src.langgraphAgentic.Tools.search_tool import create_tool_node,get_tools

class GraphBuilder:
    def __init__(self,model):
        self.llm=model
        self.graph_builder=StateGraph(state)

    def basic_chatbot_build_graph(self):
        """
        builds a basic chatbot using langgraph
        """
        print("basic_chatbot_build_graph")
        self.GroqNode=BasicChatBotnode(self.llm)
        self.graph_builder.add_node("chatbot",self.GroqNode.process)
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_edge("chatbot",END)

    def chatbot_with_tools_build_graph(self):
        """
        Builds an advanced chatbot graph with tool integration.
        This method creates a chatbot graph that includes both a chatbot node 
        and a tool node. It defines tools, initializes the chatbot with tool 
        capabilities, and sets up conditional and direct edges between nodes. 
        The chatbot node is set as the entry point.
        """
        print("chatbot_with_tools_build_graph")
        ## Define the tool and tool node

        tools=get_tools()
        tool_node=create_tool_node(tools)

        ##Define LLM
        llm = self.llm

        # Define chatbot node
        obj_chatbot_with_node = ChatbotWithToolNode(llm)
        chatbot_node = obj_chatbot_with_node.create_chatbot(tools)

        # Add nodes
        self.graph_builder.add_node("chatbot", chatbot_node)
        self.graph_builder.add_node("tools", tool_node)

        # Define conditional and direct edges
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_conditional_edges("chatbot", tools_condition)
        self.graph_builder.add_edge("tools","chatbot")


    def setupGraph(self,usecase,apiKey=None):
        if usecase=="Basic Chatbot":
            self.basic_chatbot_build_graph()
        elif usecase=="Chatbot with tool":
            self.chatbot_with_tools_build_graph()

    def get_graph(self):
        return self.graph_builder