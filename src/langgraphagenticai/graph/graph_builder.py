from langgraph.graph import StateGraph,START,END
from src.langgraphagenticai.state.state import State
from src.langgraphagenticai.nodes.chatbot import BasicChatbotNode
class GraphBuilder:
    def __init__(self,model):
        self.llm = model
        self.graph_builder = StateGraph(State)
    
    def basic_chatbot_build_graph(self):
        self.basicchatbotnode = BasicChatbotNode(self.llm)
        self.graph_builder.add_node("chatbot",self.basicchatbotnode.process)
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_edge("chatbot",END)