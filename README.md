# 🚀 Build With Me — From LLMs to Agentic AI

Welcome to the **Build With Me — Gen AI Series** repository ✨

This repository contains all the code from my Instagram/Youtube series where we learn and build Gen AI applications step by step — starting from making our first LLM call all the way to building Agentic AI systems.

The goal of this series is simple:

> Make Gen AI easy, practical, and beginner-friendly.

Whether you're:
- a student
- a beginner in AI
- preparing for Gen AI/Data Science roles
- or someone curious about how modern AI apps work

This repository is for you 🚀

---

# 📚 What You'll Learn

In this series, we build:

- LLM Applications
- Memory-based Chatbots
- Prompt Engineering Workflows
- Streamlit AI Apps
- Embeddings
- Vector Databases
- RAG Pipelines
- PDF Chatbots
- Tool Calling
- AI Agents
- Multi-Agent Systems
- Agentic AI Workflows

---

# 🛠️ Prerequisites

Before running the project, install the following:

## 1️⃣ Install Python

Download Python:

- Python Official Website: https://www.python.org/downloads/

Verify installation:

```bash
python --version
```

or

```bash
python3 --version
```

---

# ⚡ Install UV

This project uses **uv** for dependency management and execution.

Install uv:

```bash
pip install uv
```

Verify installation:

```bash
uv --version
```

---

# 📥 Clone Repository

```bash
git clone https://github.com/NavyaSai-V/Build_with_Me-GenAI-.git
```

```bash
cd Build_with_Me-GenAI-
```

---

# 🏗️ Initialize Project

```bash
uv init
```

---

# 📦 Install Dependencies

## Core Libraries

```bash
uv add google-genai python-dotenv
```

## Streamlit

```bash
uv add streamlit
```

## Vector Database

```bash
uv add chromadb
```

## PDF Processing

```bash
uv add PyPDF2
```

---

# 🔑 Create Gemini API Key

1. Open Google AI Studio
2. Generate API Key
3. Copy the key

Google AI Studio:
https://aistudio.google.com/

---

# 🔐 Create .env File

Create a file named:

```bash
.env
```

Add:

```env
GEMINI_API_KEY=your_api_key_here
```

⚠️ Never expose your API key publicly.

---

# ▶️ Running Episodes

Run any episode using:

```bash
uv run episode_name.py
```

Example:

```bash
uv run episode_1.py
```

---

# 📂 Recommended Project Structure

```bash
Build_with_Me-GenAI-/
│
├── .env
├── pyproject.toml
├── README.md
│
├── episode_1.py
├── episode_2.py
├── episode_3.py
├── episode_4.py
├── episode_5.py
├── episode_6.py
├── episode_7.py
├── episode_8.py
├── episode_9.py
├── episode_10.py
├── episode_11.py
├── episode_12.py
│
├── data/
│   └── sample.pdf
```

---

# 🎬 Episode Roadmap

## Episode 1 — Your First LLM Call

### What We Build
- First Gemini API call
- Understanding APIs
- Using `.env`
- Generating AI responses

### Concepts Covered
- LLMs
- APIs
- API Keys
- Prompt → Response Flow

Run:

```bash
uv run episode_1.py
```

---

## Episode 2 — Building Memory

### What We Build
- Chat history
- Memory-based chatbot

### Concepts Covered
- messages array
- user role
- assistant role
- system role

Run:

```bash
uv run episode_2.py
```

---

## Episode 3 — Prompt Engineering

### What We Build
- Dynamic prompt interaction
- Continuous chatbot loop

### Concepts Covered
- Prompt Engineering
- Runtime input
- Prompt variations
- AI response behavior

Run:

```bash
uv run episode_3.py
```

---

## Episode 4 — Building AI UI with Streamlit

### What We Build
- First AI web application
- Streamlit UI

### Concepts Covered
- Streamlit
- Text input
- UI integration
- Web-based AI apps

Run:

```bash
uv run episode_4.py
```

Run Streamlit App:

```bash
streamlit run episode_4.py
```

---

## Episode 5 — Limitations of LLMs

### What We Learn
- Why LLMs forget
- Why LLMs don't know custom data

### Concepts Covered
- Context Window
- General Knowledge Limitation
- Introduction to Embeddings
- Introduction to Vector Databases

---

## Episode 6 — Understanding Embeddings

### What We Build
- Generate embeddings using Gemini

### Concepts Covered
- Embeddings
- Vectors
- Semantic Similarity
- Numerical Representation of Text

Run:

```bash
uv run episode_6.py
```

---

## Episode 7 — Vector Databases

### What We Build
- Store embeddings inside ChromaDB
- Perform semantic search

### Concepts Covered
- ChromaDB
- Semantic Search
- Vector Storage
- Retrieval

Run:

```bash
uv run episode_7.py
```

---

## Episode 8 — Building RAG Pipeline

### What We Build
- Retrieval Augmented Generation pipeline

### Concepts Covered
- Retrieval
- Augmentation
- Generation
- Context Injection

Run:

```bash
uv run episode_8.py
```

---

## Episode 9 — PDF Chatbot

### What We Build
- AI chatbot for PDFs

### Concepts Covered
- PDF Reading
- Chunking
- Embeddings
- Retrieval
- RAG Pipeline

Run:

```bash
uv run episode_9.py
```

---

## Episode 10 — Tool Calling

### What We Build
- LLM with external tools

### Concepts Covered
- Tool Calling
- Function Calling
- External Actions
- LLM + Tools

Run:

```bash
uv run episode_10.py
```

---

## Episode 11 — AI Agents

### What We Build
- First AI Agent

### Concepts Covered
- Reasoning
- Planning
- Tool Selection
- Autonomous Actions

Run:

```bash
uv run episode_11.py
```

---

## Episode 12 — Multi-Agent Systems

### What We Build
- Multiple AI agents collaborating

### Concepts Covered
- Multi-Agent Communication
- Specialized Agents
- Agent Workflows
- Collaboration Systems

Run:

```bash
uv run episode_12.py
```

---

# 🚀 Future Episodes

Upcoming topics:

- LangGraph
- Memory Systems
- AI Workflows
- MCP
- Agentic RAG
- Autonomous AI Systems
- Deployment
- Production AI Apps

---

# 💡 Why This Series?

Most Gen AI tutorials:
- overwhelm beginners
- skip fundamentals
- jump directly into frameworks

This series focuses on:

✅ Simplicity
✅ Practical Learning
✅ Step-by-Step Building
✅ Beginner-Friendly Explanations
✅ Real Gen AI Development

---

# 🤝 Connect With Me

📌 Instagram: Data Science with Navi

If this repository helped you:
- ⭐ Star the repo
- 🍴 Fork it
- 📢 Share it with others learning Gen AI

---

# ⚠️ Disclaimer

This repository is built for educational purposes.

Some implementations are simplified intentionally to make concepts easier for beginners to understand.

---

# ❤️ Final Note

If you're feeling overwhelmed by Gen AI...

Take it one episode at a time.

You do NOT need to learn everything in one day 🚀

