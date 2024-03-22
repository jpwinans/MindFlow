from utils import save_file, open_file

class AfflictedAgency:

    def __init__(self, agent_id):
        self.agent_id = agent_id

    def get_agent_profile(self):
        return open_file(f"profiles/{self.agent_id}_profile.txt") # TODO: get from storehouse
     