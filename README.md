<!-- ```markdown -->
# AI Workflow Automation Agent

## Overview
AI-powered system that:
1. Processes user queries
2. Performs HubSpot CRM operations
3. Sends email confirmations
Using OpenAI function calling with multi-agent architecture.

## 🚀 Quick Start

### 1. Clone Repo
```bash
git clone https://github.com/theshahzaib/ai-agent.git
cd ai-agent
```

### 2. Install Requirements
```bash
pip install -r requirements.txt
```

### 3. Configure Environment
Modify `.env` file:
```env
OPENAI_API_KEY = sk-your-key-here
HUBSPOT_API_KEY = pat-your-key-here
SENDGRID_API_KEY = SG.your-key-here
```



## 📂 File Structure
```
ai-agent/
├── README.md            # Project overview
├── agents/              # Agent implementations
│   ├── orchestrator.py  # Task delegation
│   ├── hubspot_agent.py # CRM operations
│   └── email_agent.py   # Email handling
├── utils/               # Helper functions
│   ├── config_loader.py # Config loading
│   └── error_handler.py # Error handling
├── .env                 # Environment variables
├── config.json          # API configurations
├── main.py              # Entry point
└── req.txt              # Python dependencies
```

## ⚙️ Configuration
Edit `config.json` for API endpoints:
```json
{
    "openai": {"model": "gpt-3.5-turbo"},
    "hubspot": {"api_base": "https://api.hubapi.com"},
    "sendgrid": {"api_base": "https://api.sendgrid.com/v3/"}
}
```

## 🔧 Functionality
| Agent          | Responsibilities                | API Used       |
|----------------|---------------------------------|----------------|
| Orchestrator   | Task delegation & workflow      | OpenAI         |
| HubSpot Agent  | Lead creation/management        | HubSpot CRM    |
| Email Agent    | Send notifications              | SendGrid       |

## 📦 Create Conda Enviornment
Conda environment is recommended for package management.
```bash
conda create --name agent-env python=3.11
conda activate agent-env
```

## 📦 Or Virtual Enviornment
```bash
python3 -m venv agent-env
source agent-env/bin/activate
```

## 🛠️ Configuration
1. API Errors: Verify keys in `.env`
2. Module Issues: `pip install -r requirements.txt`
3. HubSpot: Ensure developer account is activated

## 🚀 Run
```bash
python main.py
```
When prompted, enter requests like:  
"Create lead for ali@example.com at Tech Corp"

## 📜 License
MIT License - See [LICENSE](LICENSE) for details

## 📧 Contact
Developed with ❤️ by [Shahzaib Asif](https://bit.ly/shahzaibcv) -
Email: shahzaib.asif024@gmail.com

- For Aegasis Labs Assessment - AI Workflow Automation Agent