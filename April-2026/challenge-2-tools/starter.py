"""
Challenge 2: Adding Tools to Your Agent
Give your agent a calculator, weather tool, and age calculator.
Model: Amazon Nova Pro via Bedrock

Instructions:
  1. Fill in the TODO sections below
  2. Run: python starter.py
  3. Needs AWS credentials configured (aws configure)
"""

import os
os.environ["BYPASS_TOOL_CONSENT"] = "true"

from datetime import date, datetime
from strands import Agent, tool
from strands_tools import calculator

MODEL = "us.amazon.nova-pro-v1:0"


# ============================================================
# TODO 1: Create a custom weather tool
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
        import requests
        # Using wttr.in API for real weather data
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
        # Fallback to dummy data if API fails
        return f"The weather in {city} is partly cloudy, 30°C (simulated data)"


# ============================================================
# TODO 2: Create a custom age calculator tool
# ============================================================
@tool
def age_calculator(birth_date: str) -> str:
    """Calculate age from a birth date.
    
    Args:
        birth_date: Date of birth in YYYY-MM-DD format.
    
    Returns:
        The calculated age in years.
    """
    try:
        # Parse the birth date
        birth = datetime.strptime(birth_date, "%Y-%m-%d").date()
        today = date.today()
        
        # Calculate age
        age = today.year - birth.year
        
        # Adjust if birthday hasn't occurred this year yet
        if (today.month, today.day) < (birth.month, birth.day):
            age -= 1
        
        return f"Age: {age} years old (born on {birth_date})"
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD format."


# ============================================================
# TODO 3: Create an agent with all tools
# ============================================================
agent = Agent(
    model=MODEL,
    tools=[calculator, weather, age_calculator],
    system_prompt="You are a helpful assistant with access to calculator, weather, and age calculation tools. Use them when needed to answer user questions accurately."
)


# ============================================================
# TODO 4: Test the agent with different questions
# ============================================================

# Test math
print("🧮 Math test:")
response = agent("What is 42 * 17?")
print(response)

# Test weather
print("\n🌤️ Weather test:")
response = agent("What's the weather in Chennai?")
print(response)

# Test age
print("\n🎂 Age test:")
response = agent("How old is someone born on 2000-05-15?")
print(response)


print("\n✅ Challenge 2 complete!")
