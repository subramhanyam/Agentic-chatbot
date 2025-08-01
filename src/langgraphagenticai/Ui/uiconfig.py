from configparser import ConfigParser

class Config:
    def __init__(self,config_path = r"C:\Users\Administrator\Desktop\1602_24_733_186\AGENTICWORKSPACE\AGENTICCHATBOT\src\langgraphagenticai\Ui\uiconfig.ini"):
        self.configparser = ConfigParser()
        self.configparser.read(config_path)
    
    def llm_options(self):
        return self.configparser["DEFAULT"].get("llm_Option").split(", ")
    
    def usecase_options(self):
        return self.configparser["DEFAULT"].get("usecase_options").split(", ")
    
    def llm1_model_options(self):
        return self.configparser["DEFAULT"].get("llm1_model_options").split(", ")
    
    def llm2_model_options(self):
        return self.configparser["DEFAULT"].get("llm2_model_options").split(", ")
    
    def page_title(self):
        return self.configparser["DEFAULT"].get("page_title")