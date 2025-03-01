import requests
import os
from utils.error_handler import handle_api_error

class EmailAgent:
    def __init__(self, config):
        self.config = config
        self.api_key = os.getenv(self.config['api_key_env'])
        self.base_url = self.config['api_base']

    @handle_api_error
    def send_email(self, recipient_email, subject, body):
        url = f"{self.base_url}{self.config['send_email_endpoint']}"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "personalizations": [{"to": [{"email": recipient_email}]}],
            "from": {"email": "noreply@example.com"},
            "subject": subject,
            "content": [{"type": "text/plain", "value": body}]
        }
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return {"status": "success", "message": "Email sent"}