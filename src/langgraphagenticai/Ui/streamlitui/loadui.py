import streamlit as st
import os

from src.langgraphagenticai.Ui.uiconfig import Config

class Loadui:
    def __init__(self):
        self.config = Config()
        self.user_choices = {}
    def load_streamlit_ui(self):
        st.set_page_config(page_title=self.config.page_title())
        st.header(self.config.page_title())

        with st.sidebar:
            llm_options = self.config.llm_options()
            usecases = self.config.usecase_options()

            self.user_choices["select_llm"]=st.selectbox("select_llm",llm_options)
            
            
            if self.user_choices["select_llm"] == "llm1":
                model_options = self.config.llm1_model_options()
            else:
                model_options = self.config.llm2_model_options()
            
            self.user_choices["select_model_options"]=st.selectbox("select_model_options",model_options)
            self.user_choices["API_KEY"]=st.text_input("enter api key",type="password")

            if not self.user_choices["API_KEY"]:
                st.warning("please enter a api key")
            
            self.user_choices["select_usecase"]=st.selectbox("select_usecase",usecases)

        return self.user_choices