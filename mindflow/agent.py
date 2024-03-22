from agency.afflicted import AfflictedAgency
from agency.storehouse import StorehouseAgency
from agency.mental import MentalAgency

class Agency:
    def __init__(self, agent_id):
        self.afflicted = AfflictedAgency(agent_id)
        self.storehouse = StorehouseAgency(agent_id)
        self.mental = MentalAgency(agent_id)
        self.conversation = self.mental.conversation
        # self.scratchpad = self.mental.scratchpad

class Agent:
    def __init__(self, name, agent_id):
        self.name = name
        self.agent_id = agent_id
        self.agency = Agency(agent_id)
        self.profile = self.agency.afflicted.get_agent_profile()
        self.system_prompt = self.agency.mental.get_system_prompt()
    
    def add_message(self, source_agent_id, message):
        self.agency.storehouse.store_message(source_agent_id, message)

    def get_messages(self, limit=None):
        return self.agency.storehouse.remember("message", limit=limit)

    def update_conversation(self, role, message):
        self.conversation.append(f"{role} {message}")

    def get_current_profile(self):
        return self.profile
