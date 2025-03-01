import requests
import os
from utils.error_handler import handle_api_error

class HubSpotAgent:
    def __init__(self, config):
        self.config = config
        self.api_key = os.getenv(self.config['api_key_env'])
        self.base_url = self.config['api_base']

    @handle_api_error
    def create_lead(self, properties):
        url = f"{self.base_url}{self.config['create_lead_endpoint']}"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        response = requests.post(url, headers=headers, json={"properties": properties})
        response.raise_for_status()
        return {"status": "success", "message": "Lead created", "data": response.json()}