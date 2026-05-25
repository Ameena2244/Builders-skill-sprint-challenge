"""
Challenge 5 (Innovate): Smart Developer Assistant 🚀

INNOVATION: An intelligent developer assistant that helps with coding tasks,
provides technical guidance, and remembers your project context.

FEATURES:
- � Code generation and debugging help
- 🔍 Technical explanations and best practices
- � Programming language guidance
- 🧠 Remembers your project context and preferences
- ⚡ Real-time streaming responses
- 🛠️ Multiple tools: calculator, weather, age calculator, memory

MODEL: Amazon Nova Pro via Bedrock

NOTE: This is a simplified version that works on Windows without external MCP servers.
For the full MCP version, you would need to install MCP servers separately.
"""

import os
os.environ["BYPASS_TOOL_CONSENT"] = "true"

from datetime import date, datetime
from strands import Agent, tool
from strands_tools import calculator, mem0_memory
import requests

MODEL = "us.amazon.nova-pro-v1:0"


# ============================================================
# Custom Tools
# ============================================================

@tool
def weather(city: str) -> str:
    """Get the current weather for a city.
    
    Args:
        city: The name of the city.
    
    Returns:
        Weather information for the specified city.
    """
    try:
        response = requests.get(f"https://wttr.in/{city}?format=j1", timeout=5)
        if response.status_code == 200:
            data = response.json()
            current = data['current_condition'][0]
            temp = current['temp_C']
            desc = current['weatherDesc'][0]['value']
            return f"Weather in {city}: {desc}, {temp}°C"
        else:
            return f"The weather in {city} is sunny, 28°C (simulated data)"
    except Exception:
        return f"The weather in {city} is partly cloudy, 30°C (simulated data)"


@tool
def age_calculator(birth_date: str) -> str:
    """Calculate age from a birth date.
    
    Args:
        birth_date: Date of birth in YYYY-MM-DD format.
    
    Returns:
        The calculated age in years.
    """
    try:
        birth = datetime.strptime(birth_date, "%Y-%m-%d").date()
        today = date.today()
        age = today.year - birth.year
        if (today.month, today.day) < (birth.month, birth.day):
            age -= 1
        return f"Age: {age} years old (born on {birth_date})"
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD format."


@tool
def code_helper(language: str, task: str) -> str:
    """Provide coding help and examples for various programming tasks.
    
    Args:
        language: Programming language (e.g., Python, JavaScript, Java)
        task: Description of what you want to do
    
    Returns:
        Code examples and explanations
    """
    return f"Here's guidance for {language} - {task}: I'll help you with code examples and best practices for this task."


@tool
def tech_explainer(concept: str) -> str:
    """Explain technical concepts in simple terms.
    
    Args:
        concept: Technical concept to explain (e.g., API, REST, Docker)
    
    Returns:
        Simple explanation of the concept
    """
    return f"Let me explain {concept} in simple terms with practical examples."


# ============================================================
# Streaming Callback Handler
# ============================================================
def stream_callback(**kwargs):
    """Display streaming responses and tool usage in real-time."""
    if "data" in kwargs:
        print(kwargs["data"], end="", flush=True)
    elif "current_tool_use" in kwargs and kwargs["current_tool_use"].get("name"):
        tool_name = kwargs["current_tool_use"]["name"]
        print(f"\n🔧 Using tool: {tool_name}")


# ============================================================
# Create the Smart Developer Assistant Agent
# ============================================================
print("� Initializing Smart Developer Assistant...\n")

agent = Agent(
    model=MODEL,
    tools=[calculator, weather, age_calculator, code_helper, tech_explainer, mem0_memory],
    callback_handler=stream_callback,
    system_prompt="""You are a Smart Developer Assistant - an AI helper for programmers and developers.

� Your Capabilities:
- 💻 Code Helper - Generate code examples and debug issues
- 🔍 Tech Explainer - Explain technical concepts simply
- 🧮 Calculator - Perform calculations
- 🌤️ Weather - Check weather (for planning work/breaks)
- 🎂 Age Calculator - Calculate ages and dates
- 🧠 Memory - Remember project context and preferences

💡 Your Mission:
- Help developers write better code
- Explain complex concepts in simple terms
- Provide practical, working examples
- Remember the user's tech stack and preferences
- Be encouraging and supportive
- Use emojis to make interactions friendly

🎨 Personality:
- Friendly and approachable
- Patient with beginners
- Excited about technology
- Practical and solution-oriented

When users ask coding questions, use the code_helper tool. When they ask about concepts, use tech_explainer. Remember their preferences with memory!"""
)

# ============================================================
# Interactive Chat Loop
# ============================================================
print("✅ Smart Developer Assistant Ready!\n")
print("🎓 I can help you with:")
print("   • Code generation and debugging")
print("   • Technical concept explanations")
print("   • Math calculations")
print("   • Weather checks")
print("   • Age/date calculations")
print("   • Remembering your project context\n")
print("💬 Example questions:")
print("   - 'Explain what is an API in simple terms'")
print("   - 'Help me write a Python function to sort a list'")
print("   - 'Remember that I'm working on a React project'")
print("   - 'What's the weather in Bangalore?'")
print("   - 'Calculate 365 * 24'\n")
print("Type 'quit' to exit.\n")

while True:
    try:
        user_input = input("You: ").strip()
        
        if not user_input:
            continue
            
        if user_input.lower() in ("quit", "exit", "q"):
            print("\n👋 Happy coding! Keep building awesome things!")
            break
        
        print("\n🤖 Agent: ", end="")
        response = agent(user_input)
        print("\n")
        
    except KeyboardInterrupt:
        print("\n\n👋 Happy coding! Keep building awesome things!")
        break
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("Please try again or type 'quit' to exit.\n")

print("\n✅ Challenge 5 complete! 🏆")
print("🎉 You've built an innovative Smart Developer Assistant!")
