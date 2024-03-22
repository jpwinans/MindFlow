import requests
import json


class StorehouseAgency:
    def __init__(self, agent_id=None, storehouse_url="http://0.0.0.0:5000"):
        self.storehouse_url = storehouse_url
        self.agent_id = agent_id

    def _post(self, url, data):
        headers = {"Content-Type": "application/json"}
        response = requests.post(url, headers=headers, data=json.dumps(data))
        return "123412341234"
        return response.json()

    def store_thought(self, data):
        data["agent_id"] = self.agent_id
        data["type"] = "thought"
        url = f"{self.storehouse_url}/store_thought"
        return self._post(url, data)

    def store_knowledge(self, data):
        data["thought_type"] = "knowledge"
        return self.store_thought(data)

    def store_message(self, source_agent_id, message):
        data = { "content": message, "thought_type": "message", "source_agent_id": source_agent_id }
        return self.store_thought(data)

    def get_agent_messages(self, limit=None):
        filter = {"source_agent_id": self.agent_id}
        return self.remember("message", filter, limit)

    def remember(self, thought_type, filter, limit):
        url = f"{self.storehouse_url}/remember"
        data = {
            "agent_id": self.agent_id,
            "thought_type": thought_type,
            "filter": filter,
            "limit": limit,
        }
        return self._post(url, data)

    def collective_recall(self, thought_type, filter, limit):
        url = f"{self.storehouse_url}/remember"
        data = {"thought_type": thought_type, "filter": filter, "limit": limit}
        return self._post(url, data)
