import os
import json
import openai
from agents.orchestrator import get_function_definitions, orchestrate
from agents.hubspot_agent import HubSpotAgent
from agents.email_agent import EmailAgent
from utils.config_loader import load_config

def main():
    config = load_config()
    openai.api_key = os.getenv(config['openai']['api_key_env'])
    
    hubspot_agent = HubSpotAgent(config['hubspot'])
    email_agent = EmailAgent(config['sendgrid'])
    
    messages = [{
        "role": "system",
        "content": "You are an orchestrator that manages workflows. Create leads and send confirmation emails."
    }]
    
    functions = get_function_definitions()
    
    user_query = input("Enter your request: ")
    
    while True:
        response_message = orchestrate(user_query, messages, functions)
        
        if hasattr(response_message, 'function_call'):
            func_name = response_message.function_call.name
            args = json.loads(response_message.function_call.arguments)
            
            if func_name == "create_lead":
                result = hubspot_agent.create_lead(args)
            elif func_name == "send_email":
                result = email_agent.send_email(**args)
            else:
                result = {"status": "error", "message": "Unknown function"}
            
            messages.append({
                "role": "function",
                "name": func_name,
                "content": json.dumps(result)
            })
        else:
            print("\nFinal Response:", response_message.content)
            break

if __name__ == "__main__":
    main()