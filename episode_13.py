# =========================================================
# EPISODE 13
# REAL-TIME INTERNET ACCESS AI
# USING TAVILY SEARCH API
# =========================================================

# INSTALL:
# pip install google-generativeai python-dotenv tavily-python

# =========================================================
# GET API KEYS
# =========================================================
#
# GEMINI API:
# https://aistudio.google.com/app/apikey
#
# TAVILY API:
# https://app.tavily.com/
#
# =========================================================


import os
from dotenv import load_dotenv

import google.generativeai as genai

from tavily import TavilyClient


# =========================================================
# LOAD ENV VARIABLES
# =========================================================

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")


# =========================================================
# CONFIGURE GEMINI
# =========================================================

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


# =========================================================
# CONFIGURE TAVILY
# =========================================================

tavily_client = TavilyClient(api_key=TAVILY_API_KEY)


# =========================================================
# REAL WEB SEARCH TOOL
# =========================================================

def web_search(query):

    """
    Real-time web search using Tavily
    """

    print("\n🌐 SEARCHING INTERNET...\n")

    response = tavily_client.search(

        query=query,

        search_depth="basic",

        max_results=5
    )

    results = response["results"]

    formatted_results = ""

    for idx, result in enumerate(results, start=1):

        formatted_results += f"""
        RESULT {idx}

        TITLE:
        {result['title']}

        CONTENT:
        {result['content']}

        URL:
        {result['url']}

        ---------------------------
        """

    return formatted_results


# =========================================================
# AVAILABLE TOOLS
# =========================================================

TOOLS = {

    "web_search": web_search

}


# =========================================================
# SYSTEM PROMPT
# =========================================================

SYSTEM_PROMPT = """
You are an intelligent AI assistant.

You have access to internet search tools.

IMPORTANT:

If the user asks:
- latest news
- current events
- viral trends
- live scores
- recent updates

then use the web_search tool.

STRICTLY return ONLY:

TOOL: web_search
INPUT: search query

Do not add explanations.
Do not add extra text.

If internet is not required,
answer normally.
"""


# =========================================================
# ASK GEMINI
# =========================================================

def ask_gemini(user_query):

    prompt = f"""
    {SYSTEM_PROMPT}

    USER QUESTION:
    {user_query}
    """

    response = model.generate_content(prompt)

    return response.text.strip()


# =========================================================
# PARSE TOOL CALL
# =========================================================

def parse_tool_call(response_text):

    if "TOOL:" not in response_text:
        return None, None

    lines = response_text.split("\n")

    tool_name = None
    tool_input = None

    for line in lines:

        if line.startswith("TOOL:"):
            tool_name = line.replace("TOOL:", "").strip()

        if line.startswith("INPUT:"):
            tool_input = line.replace("INPUT:", "").strip()

    return tool_name, tool_input


# =========================================================
# MAIN AI AGENT
# =========================================================

def run_ai_agent(user_query):

    print("\n======================================")
    print("USER QUESTION:")
    print(user_query)
    print("======================================\n")

    # -------------------------------------------------
    # STEP 1 → ASK GEMINI
    # -------------------------------------------------

    response = ask_gemini(user_query)

    print("GEMINI RESPONSE:")
    print(response)

    # -------------------------------------------------
    # STEP 2 → CHECK TOOL CALL
    # -------------------------------------------------

    tool_name, tool_input = parse_tool_call(response)

    # -------------------------------------------------
    # STEP 3 → NORMAL RESPONSE
    # -------------------------------------------------

    if tool_name is None:

        print("\nFINAL ANSWER:")
        print(response)

        return

    print("\n🤖 AI DECIDED TO USE INTERNET TOOL")
    print(f"TOOL: {tool_name}")

    # -------------------------------------------------
    # STEP 4 → EXECUTE WEB SEARCH
    # -------------------------------------------------

    tool_function = TOOLS.get(tool_name)

    if tool_function is None:

        print("Tool not found")
        return

    web_results = tool_function(tool_input)

    print("\n======================================")
    print("LIVE INTERNET RESULTS")
    print("======================================\n")

    print(web_results)

    # -------------------------------------------------
    # STEP 5 → FINAL AI RESPONSE
    # -------------------------------------------------

    final_prompt = f"""
    USER QUESTION:
    {user_query}

    INTERNET SEARCH RESULTS:
    {web_results}

    Generate a clean and helpful response
    based on the latest information.
    """

    final_response = model.generate_content(final_prompt)

    print("\n======================================")
    print("FINAL AI RESPONSE")
    print("======================================\n")

    print(final_response.text)


# =========================================================
# MAIN PROGRAM
# =========================================================

if __name__ == "__main__":

    print("\n")
    print("======================================")
    print("EPISODE 13 — REAL-TIME AI INTERNET ACCESS")
    print("======================================")
    print("\n")

    while True:

        query = input("Ask something: ")

        if query.lower() == "exit":
            break

        run_ai_agent(query)
