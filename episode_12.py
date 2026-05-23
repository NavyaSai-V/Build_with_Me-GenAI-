# =========================================================
# EPISODE 12
# AI MEMORY SYSTEM
# "Without memory, AI resets every conversation."
# =========================================================

# INSTALL:
# pip install google-generativeai python-dotenv

# =========================================================
# PROJECT FLOW
# =========================================================
#
# USER MESSAGE
#       ↓
# STORE IN MEMORY
#       ↓
# SEND MEMORY + NEW MESSAGE TO AI
#       ↓
# AI GENERATES CONTEXTUAL RESPONSE
#
# =========================================================


import os
from dotenv import load_dotenv
import google.generativeai as genai


# =========================================================
# LOAD ENV VARIABLES
# =========================================================

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)


# =========================================================
# GEMINI MODEL
# =========================================================

model = genai.GenerativeModel("gemini-2.5-flash")


# =========================================================
# MEMORY STORAGE
# =========================================================

chat_history = []


# =========================================================
# STORE MEMORY
# =========================================================

def store_memory(role, message):

    chat_history.append({
        "role": role,
        "message": message
    })


# =========================================================
# GET MEMORY CONTEXT
# =========================================================

def get_memory_context():

    context = ""

    for chat in chat_history:

        context += f"{chat['role']}: {chat['message']}\n"

    return context


# =========================================================
# AI CHAT FUNCTION
# =========================================================

def chat_with_memory(user_message):

    # -----------------------------------------
    # STORE USER MESSAGE
    # -----------------------------------------

    store_memory("User", user_message)

    # -----------------------------------------
    # GET MEMORY CONTEXT
    # -----------------------------------------

    memory_context = get_memory_context()

    # -----------------------------------------
    # PROMPT
    # -----------------------------------------

    prompt = f"""
    You are a helpful AI assistant.

    Below is the conversation memory.

    MEMORY:
    {memory_context}

    Use this memory to answer naturally
    and remember previous user information.

    USER:
    {user_message}
    """

    # -----------------------------------------
    # GEMINI RESPONSE
    # -----------------------------------------

    response = model.generate_content(prompt)

    ai_response = response.text

    # -----------------------------------------
    # STORE AI RESPONSE
    # -----------------------------------------

    store_memory("AI", ai_response)

    return ai_response


# =========================================================
# DISPLAY MEMORY
# =========================================================

def display_memory():

    print("\n")
    print("======================================")
    print("CURRENT MEMORY")
    print("======================================")

    for item in chat_history:

        print(f"\n{item['role']}:")
        print(item['message'])

    print("\n")


# =========================================================
# MAIN PROGRAM
# =========================================================

if __name__ == "__main__":

    print("\n")
    print("======================================")
    print("EPISODE 12 — AI MEMORY SYSTEM")
    print("======================================")
    print("\n")

    print("Type 'memory' to view stored memory")
    print("Type 'exit' to stop\n")

    while True:

        user_input = input("You: ")

        # -----------------------------------------
        # EXIT
        # -----------------------------------------

        if user_input.lower() == "exit":
            break

        # -----------------------------------------
        # DISPLAY MEMORY
        # -----------------------------------------

        if user_input.lower() == "memory":

            display_memory()
            continue

        # -----------------------------------------
        # AI RESPONSE
        # -----------------------------------------

        ai_reply = chat_with_memory(user_input)

        print("\nAI:")
        print(ai_reply)
        print("\n")

