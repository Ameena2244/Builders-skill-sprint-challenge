"""
Challenge 1: Your First AI Agent
Build a simple agent using Strands SDK + Ollama (runs locally!)

Instructions:
  1. Fill in the TODO sections below
  2. Run: python starter.py
  3. Make sure 'ollama serve' is running in another terminal
"""

# TODO 1: Import Agent from strands
from strands import Agent

# TODO 2: Import OllamaModel from strands
from strands.models.ollama import OllamaModel

# TODO 3: Create an OllamaModel instance
# Using local Ollama server with llama3.2:3b model
ollama_model = OllamaModel(
    host="http://localhost:11434",
    model_id="gemma3:270m"
)

# TODO 4: Create an Agent with the ollama_model
# Agent with a helpful system prompt
agent = Agent(
    model=ollama_model,
    tools=[],
    system_prompt="You are a helpful assistant. Be brief and informative."
)

# TODO 5: Ask the agent a question and print the response
print("🤖 Agent: ", end="")
response = agent("Tell me a fun fact about Python programming")
print(response)

print("\n✅ Challenge 1 complete!")
