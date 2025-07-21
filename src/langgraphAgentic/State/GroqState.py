from pydantic import BaseModel,Field
from typing_extensions import TypedDict,Annotated
from langgraph.graph.message import add_messages


class state(TypedDict):
    """
    Represents the structure of the state used in the graph
    """
    messages:Annotated[list["str"],add_messages]