import streamlit as st
import os

from src.langgraphagenticai.Ui.streamlitui.loadui import Loadui

def load_agentic_ai_app():

    ui = Loadui()
    user_input = ui.load_streamlit_ui()

    user_message = st.chat_input("enter something")
    if user_message:
        st.write(user_message)