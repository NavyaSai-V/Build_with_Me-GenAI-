
# INSTALL:
# pip install google-generativeai python-dotenv requests

# =========================================================
# PROJECT FLOW
# =========================================================
#
# User Question
#        ↓
# Gemini decides:
# "Do I need a tool?"
#        ↓
# Calls Tool
#        ↓
# Tool Executes
#        ↓
# Result Returned to Gemini
#        ↓
# Final AI Response
#
# =========================================================


import os
import requests
from dotenv import load_dotenv
import google.generativeai as genai


# =========================================================
# LOAD ENV VARIABLES
# =========================================================

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)


# =========================================================
# TOOL 1 — CALCULATOR TOOL
# =========================================================

def calculator(expression):

    """
    Simple calculator tool
    """

    try:
        result = eval(expression)

        return {
            "status": "success",
            "result": result
        }

    except Exception as e:

        return {
            "status": "error",
            "message": str(e)
        }


# =========================================================
# TOOL 2 — IPL SCORE TOOL
# =========================================================

def get_ipl_score():

    """
    Fake IPL live score tool
    (For demo purpose)
    """

    score = {
        "match": "RCB vs CSK",
        "score": "RCB 178/4",
        "overs": "18.2",
        "status": "RCB needs 24 runs in 10 balls"
    }

    return score


# =========================================================
# TOOL 3 — WEATHER TOOL
# =========================================================

def get_weather(city):

    """
    Fake weather tool
    """

    weather_data = {
        "Hyderabad": "32°C, Sunny",
        "Mumbai": "29°C, Humid",
        "Bangalore": "26°C, Cloudy"
    }

    return weather_data.get(city, "Weather data not found")


# =========================================================
# AVAILABLE TOOLS
# =========================================================

TOOLS = {

    "calculator": calculator,
    "get_ipl_score": get_ipl_score,
    "get_weather": get_weather

}


# =========================================================
# GEMINI MODEL
# =========================================================

model = genai.GenerativeModel("gemini-2.5-flash")


# =========================================================
# SYSTEM PROMPT
# =========================================================

SYSTEM_PROMPT = """
You are a helpful AI assistant.

You have access to tools.

IMPORTANT:
- Decide intelligently when to use tools.
- Use calculator for math.
- Use get_ipl_score for IPL score questions.
- Use get_weather for weather questions.

Return ONLY the tool call in this format:

TOOL: tool_name
INPUT: input_data

If no tool is needed,
answer normally.
"""


# =========================================================
# FUNCTION:
# ASK GEMINI
# =========================================================

def ask_gemini(user_query):

    prompt = f"""
    {SYSTEM_PROMPT}

    USER QUESTION:
    {user_query}
    """

    response = model.generate_content(prompt)

    return response.text


# =========================================================
# FUNCTION:
# PARSE TOOL CALL
# =========================================================

def parse_tool_call(response_text):

    """
    Extract tool name and input
    """

    if "TOOL:" not in response_text:
        return None, None

    lines = response_text.strip().split("\n")

    tool_name = None
    tool_input = None

    for line in lines:

        if line.startswith("TOOL:"):
            tool_name = line.replace("TOOL:", "").strip()

        if line.startswith("INPUT:"):
            tool_input = line.replace("INPUT:", "").strip()

    return tool_name, tool_input


# =========================================================
# MAIN AI PIPELINE
# =========================================================

def run_ai_agent(user_query):

    print("\n==============================")
    print("USER QUESTION:")
    print(user_query)
    print("==============================\n")

    # -------------------------------------------------
    # STEP 1:
    # Ask Gemini
    # -------------------------------------------------

    response = ask_gemini(user_query)

    print("GEMINI RESPONSE:")
    print(response)

    # -------------------------------------------------
    # STEP 2:
    # Check if tool needed
    # -------------------------------------------------

    tool_name, tool_input = parse_tool_call(response)

    # -------------------------------------------------
    # STEP 3:
    # If no tool needed
    # -------------------------------------------------

    if tool_name is None:

        print("\nFINAL ANSWER:")
        print(response)

        return

    print("\nAI DECIDED TO USE TOOL:")
    print(tool_name)

    # -------------------------------------------------
    # STEP 4:
    # Execute Tool
    # -------------------------------------------------

    tool_function = TOOLS.get(tool_name)

    if tool_function is None:

        print("Tool not found")
        return

    print("\nEXECUTING TOOL...\n")

    # Handle tools with/without input

    try:

        # Tools WITHOUT input
        if tool_name == "get_ipl_score":

            tool_result = tool_function()

        # Tools WITH input
        else:

            tool_result = tool_function(tool_input)

    except Exception as e:

        tool_result = {
            "status": "error",
            "message": str(e)
        }

    print("TOOL RESULT:")
    print(tool_result)

    # -------------------------------------------------
    # STEP 5:
    # Send tool result back to Gemini
    # -------------------------------------------------

    final_prompt = f"""
    USER QUESTION:
    {user_query}

    TOOL RESULT:
    {tool_result}

    Generate a final helpful response for the user.
    """

    final_response = model.generate_content(final_prompt)

    print("\n==============================")
    print("FINAL AI RESPONSE:")
    print(final_response.text)
    print("==============================\n")


# =========================================================
# TEST CASES
# =========================================================

if __name__ == "__main__":

    print("\n")
    print("======================================")
    print("EPISODE 10 — AI TOOLS / FUNCTION CALLING")
    print("======================================")
    print("\n")

    while True:

        query = input("Ask something: ")

        if query.lower() == "exit":
            break

        run_ai_agent(query)