from src.langgraphAgentic.State.GroqState import state

class BasicChatBotnode:
    """
    basic chat bot node implementation
    """
    def __init__(self,model):
        self.llm=model
    
    def process(self,state:state)->dict:
        """
        process the state and generate a chatresponse
        """
        return {"messages":self.llm.invoke(state['messages'])}
