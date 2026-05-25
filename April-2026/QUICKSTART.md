# 🚀 Quick Start Guide

Get up and running with all 5 challenges in minutes!

## ⚡ Fast Setup (5 minutes)

### Step 1: Install Dependencies
```bash
cd April-2026
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
```

### Step 2: Verify Installation
```bash
python verify_setup.py
```

### Step 3: Choose Your Path

#### Path A: Start with Ollama (Challenge 1 - Local)
```bash
# Install Ollama
# Windows: Download from ollama.com/download
# macOS: brew install ollama
# Linux: curl -fsSL https://ollama.com/install.sh | sh

# Start Ollama (keep this running)
ollama serve

# In new terminal: Pull model
ollama pull llama3.2:3b

# Run Challenge 1
cd challenge-1-first-agent
python starter.py
```

#### Path B: Start with AWS Bedrock (Challenges 2-5)
```bash
# Configure AWS
aws configure
# Enter: Access Key, Secret Key, Region (us-east-1)

# Enable Nova Pro in AWS Console:
# https://console.aws.amazon.com/bedrock → Model Access → Enable Nova Pro

# Run Challenge 2
cd challenge-2-tools
python starter.py
```

## 📚 Challenge Overview

| # | Name | Time | Difficulty |
|---|------|------|-----------|
| 1 | First Agent (Ollama) | 5 min | ⭐ Easy |
| 2 | Tools (Bedrock) | 10 min | ⭐⭐ Medium |
| 3 | Memory (Bedrock) | 10 min | ⭐⭐ Medium |
| 4 | Full Agent (Bedrock) | 15 min | ⭐⭐⭐ Hard |
| 5 | MCP Agent (Bedrock) | 20 min | 🚀 Innovate |

## 🎯 What Each Challenge Does

### Challenge 1: First Agent
```
You: Tell me a fun fact about Python
Agent: Python is named after Monty Python...
```

### Challenge 2: Tools
```
You: What is 42 * 17?
Agent: 714

You: What's the weather in Chennai?
Agent: Weather in Chennai: Partly cloudy, 33°C
```

### Challenge 3: Memory
```
You: Remember my name is Ravi
Agent: ✅ I'll remember that!

You: What's my name?
Agent: Your name is Ravi!
```

### Challenge 4: Full Agent
```
You: What's the weather in Delhi and calculate 365 * 24
🔧 Using tool: weather
🔧 Using tool: calculator
Agent: Weather in Delhi is sunny, 28°C. 365 × 24 = 8,760
```

### Challenge 5: AWS Documentation Expert
```
You: What is AWS Lambda?
🔧 Using tool: search_aws_documentation
Agent: AWS Lambda is a serverless compute service that lets you run code...
```

## 🐛 Common Issues

### "Module not found"
```bash
pip install -r requirements.txt
```

### "Ollama connection refused"
```bash
# Make sure Ollama is running
ollama serve
```

### "AWS credentials not found"
```bash
aws configure
```

### "Bedrock access denied"
- Go to AWS Bedrock Console
- Click "Model Access"
- Enable "Amazon Nova Pro"

## 📸 Taking Screenshots

For submission, capture:
1. Terminal showing the command you ran
2. Agent's response
3. Any tool usage indicators (🔧)

## 📤 Submission

1. Complete all challenges
2. Take screenshots
3. Submit at: https://www.awsugmdu.in/

## 💡 Pro Tips

- **Challenge 1**: Try changing the system prompt to make the agent talk like a pirate! 🏴‍☠️
- **Challenge 2**: Ask questions that need multiple tools at once
- **Challenge 3**: Quit and restart to verify memory persists
- **Challenge 4**: Have a full conversation using all features
- **Challenge 5**: Customize the agent for your own use case!

## 🆘 Need Help?

Check `SOLUTION_GUIDE.md` for:
- Detailed explanations of each implementation
- Complete testing instructions
- Troubleshooting guide
- Code walkthrough

## 🎉 You're Ready!

Pick a challenge and start building! Each one takes 5-20 minutes.

Happy coding! 🚀
