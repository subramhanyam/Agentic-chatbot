from typing_extensions import TypedDict
from typing import List,Annotated
from langgraph.graph.message import add_messages

class State(TypedDict):
    messages : Annotated[List,add_messages]
