# =========================================================
# EPISODE 11
# MULTI AGENT AI SYSTEM
# "One AI thinks. Multiple AI agents collaborate."
# =========================================================

# INSTALL:
# pip install google-generativeai python-dotenv

# =========================================================
# PROJECT IDEA
# =========================================================
#
# USER TASK
#      ↓
# MANAGER AGENT
#      ↓
# RESEARCH AGENT
#      ↓
# WRITER AGENT
#      ↓
# REVIEW AGENT
#      ↓
# FINAL RESPONSE
#
# =========================================================


import os
from dotenv import load_dotenv
import google.generativeai as genai


# =========================================================
# LOAD API KEY
# =========================================================

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)


# =========================================================
# GEMINI MODEL
# =========================================================

model = genai.GenerativeModel("gemini-2.5-flash")


# =========================================================
# HELPER FUNCTION
# =========================================================

def ask_gemini(prompt):

    response = model.generate_content(prompt)

    return response.text


# =========================================================
# RESEARCH AGENT
# =========================================================

def research_agent(user_query):

    print("\n==============================")
    print("RESEARCH AGENT WORKING...")
    print("==============================\n")

    prompt = f"""
    You are a Research Agent.

    Your job:
    - Gather information
    - Extract important insights
    - Provide structured research

    USER QUERY:
    {user_query}

    Give detailed research points.
    """

    response = ask_gemini(prompt)

    print("RESEARCH AGENT OUTPUT:\n")
    print(response)

    return response


# =========================================================
# WRITER AGENT
# =========================================================

def writer_agent(research_data):

    print("\n==============================")
    print("WRITER AGENT WORKING...")
    print("==============================\n")

    prompt = f"""
    You are a Content Writer Agent.

    Your job:
    - Convert research into clean content
    - Make it easy to understand
    - Structure properly

    RESEARCH DATA:
    {research_data}

    Create a professional report.
    """

    response = ask_gemini(prompt)

    print("WRITER AGENT OUTPUT:\n")
    print(response)

    return response


# =========================================================
# REVIEW AGENT
# =========================================================

def review_agent(draft_content):

    print("\n==============================")
    print("REVIEW AGENT WORKING...")
    print("==============================\n")

    prompt = f"""
    You are a Review Agent.

    Your responsibilities:
    - Improve clarity
    - Fix mistakes
    - Improve readability
    - Ensure professional quality

    DRAFT CONTENT:
    {draft_content}

    Return the improved final version.
    """

    response = ask_gemini(prompt)

    print("REVIEW AGENT OUTPUT:\n")
    print(response)

    return response


# =========================================================
# MANAGER AGENT
# =========================================================

def manager_agent(user_query):

    print("\n")
    print("======================================")
    print("MANAGER AGENT STARTED WORKFLOW")
    print("======================================")

    # -------------------------------------------------
    # STEP 1 → RESEARCH
    # -------------------------------------------------

    research_output = research_agent(user_query)

    # -------------------------------------------------
    # STEP 2 → WRITING
    # -------------------------------------------------

    writer_output = writer_agent(research_output)

    # -------------------------------------------------
    # STEP 3 → REVIEW
    # -------------------------------------------------

    final_output = review_agent(writer_output)

    print("\n")
    print("======================================")
    print("FINAL OUTPUT TO USER")
    print("======================================\n")

    print(final_output)

    return final_output


# =========================================================
# MAIN PROGRAM
# =========================================================

if __name__ == "__main__":

    print("\n")
    print("======================================")
    print("EPISODE 11 — MULTI AGENT AI SYSTEM")
    print("======================================")
    print("\n")

    while True:

        user_query = input("Enter your task: ")

        if user_query.lower() == "exit":
            break

        manager_agent(user_query)