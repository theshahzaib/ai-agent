import openai
import json

def get_function_definitions():
    return [
        {
            "name": "create_lead",
            "description": "Create a new lead in HubSpot CRM",
            "parameters": {
                "type": "object",
                "properties": {
                    "email": {"type": "string", "description": "Lead's email address"},
                    "firstname": {"type": "string", "description": "Lead's first name"},
                    "lastname": {"type": "string", "description": "Lead's last name"},
                    "company": {"type": "string", "description": "Lead's company"}
                },
                "required": ["email"]
            }
        },
        {
            "name": "send_email",
            "description": "Send confirmation email",
            "parameters": {
                "type": "object",
                "properties": {
                    "recipient_email": {"type": "string", "description": "Recipient's email"},
                    "subject": {"type": "string", "description": "Email subject"},
                    "body": {"type": "string", "description": "Email content"}
                },
                "required": ["recipient_email", "subject", "body"]
            }
        }
    ]

def orchestrate(user_query, messages, functions):
    messages.append({"role": "user", "content": user_query})
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        functions=functions,
        function_call="auto"
    )
    
    return response.choices[0].message