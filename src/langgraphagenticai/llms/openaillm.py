import os
import streamlit as st
from langchain_openai import ChatOpenAI

class Openaillm:
    def __init__(self,user_choices):
        self.user_choices = user_choices

    def get_llm(self):
        try:
            model = self.user_choices["select_model_options"]
            api_key = self.user_choices["API_KEY"]
            llm = ChatOpenAI(model=model , api_key=api_key)
        
        except Exception as e :
            raise ValueError(f"Error has occured as:{e}")
        return llm