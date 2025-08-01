import streamlit as st
import os
from src.langgraphagenticai.llms.openaillm import Openaillm
from src.langgraphagenticai.Ui.streamlitui.loadui import Loadui
from src.langgraphagenticai.graph.graph_builder import GraphBuilder
from src.langgraphagenticai.Ui.streamlitui.display_result import DisplayResult

def load_agentic_ai_app():

    ui = Loadui()
    user_input = ui.load_streamlit_ui()

    user_message = st.chat_input("enter something")
    if user_message:
        obj_llm = Openaillm(user_input)
        llm = obj_llm.get_llm()

        use_case = user_input.get("select_usecase")
        graph_builder = GraphBuilder(llm)
        graph = graph_builder.set_usecase(use_case)
        DisplayResult(use_case,graph,user_message).display_result()
        
