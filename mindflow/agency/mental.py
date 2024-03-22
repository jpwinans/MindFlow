import requests
import json
from agency.storehouse import StorehouseAgency
from utils import open_file


class MentalAgency:
    def __init__(self, mental_url="http://0.0.0.0:1", agent_id=None):
        self.mental_url = mental_url
        self.agent_id = agent_id
        self.storehouse = StorehouseAgency(agent_id=agent_id)
        # self.scratchpad = self.load_chat_logs()
        self.conversation = []

    def get_system_prompt(self):
        system_prompt = open_file(f"mindflow/prompts/agents/{self.agent_id}_default.txt") 
        if not system_prompt:
            system_prompt = open_file("mindflow/prompts/agent_default.txt") 
        


    