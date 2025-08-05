# 🧠 AgenticOpsSuite

> AgenticOpsSuite is an agentic AI platform that intelligently analyzes CI logs, detects AMD GPU regressions, performs auto-bisect, and suggests fixes via LLMs. Designed for real-world engineering workflows, it brings self-healing CI and GPU awareness to DevOps automation.

---

## 🔥 Key Features

- ✅ **LLM-powered CI Log Analysis**
- 🚀 **Auto-Bisect Engine** with AI-suggested patches
- 🧪 **GPU Runtime & ROCm Profiler Integration**
- 🧠 **Agentic Reasoning Flow** with LangGraph
- 🧰 **Modular Tools** for CI, log triage, and observability
- 📊 **Gradio UI + FastAPI endpoint** for interaction
- 🛠️ **Offline Inference** using Ollama / Hugging Face Spaces

---

## 🎯 Use Case

Imagine a CI workflow for AMD GPU workloads:
- A test fails or ROCm profiler detects GPU slowdown
- Logs are uploaded automatically to AgenticOpsSuite
- The agentic AI system classifies the failure, matches known patterns, and provides suggestions
- If a regression is suspected, it launches an auto-bisect job and optionally proposes a code fix

---

## ⚙️ Architecture

app/ # Core service logic + API endpoints
agents/ # LangGraph agent implementations
bisect/ # Auto-bisect workflow logic and patch generation
ci/ # GitHub Actions workflows and automation
logs/ # Sample AMD GPU logs for testing
vectorstore/ # Indexed documents and embeddings for RAG
ui/ # Gradio or Streamlit user interface
demo_script.md # Step-by-step narration for demo and interviews


<img width="303" height="605" alt="Screenshot 2025-08-04 at 6 17 42 PM" src="https://github.com/user-attachments/assets/074263a2-7f33-4ca3-9cb8-9f33d2e170ef" />


---

## 🧱 Tech Stack

| Layer         | Technology                      |
|---------------|----------------------------------|
| Agentic Logic | LangGraph + LangChain           |
| Vector DB     | FAISS + Custom Document Parser  |
| LLM Inference | Ollama (Mistral, Phi-3) / Hugging Face |
| GPU Detection | PyTorch + ROCm Tools            |
| Profiling     | µProf / rocprof Integration     |
| UI/API        | Gradio + FastAPI                |
| CI/CD         | GitHub Actions                  |

---

## 🚀 Quickstart

```bash
git clone https://github.com/YOUR_USERNAME/AgenticOpsSuite.git
cd AgenticOpsSuite
pip install -r requirements.txt
ollama run mistral  # or phi3
python app/main.py  # Launches the FastAPI service

python ui/interface.py

📁 Project Structure

app/              # Core service logic + endpoints
agents/           # LangGraph agents
bisect/           # Auto-bisect workflow logic
ci/               # GitHub Actions workflows
logs/             # Sample GPU logs
vectorstore/      # Indexed documents
ui/               # Gradio or Streamlit UI
demo_script.md    # Narration for demo

🤖 Demo Use Cases
Log upload → GPU fault detected → fix suggested

ROCm profiler report → Agent flags perf bottleneck

CI test fails → auto-bisect finds culprit + patch PR

Developer runs Gradio UI to interact with logs manually

Here's a production-ready requirements.txt for your AgenticOpsSuite, supporting:

LangChain / LangGraph for agent workflows

FAISS for local vector store

Gradio for the UI

FastAPI for the service layer

Torch for GPU detection / model testing

Optional: Hugging Face inference and GitHub Actions integration


# Core LLM + Agentic Framework
langchain>=0.2.0
langgraph>=0.0.33
faiss-cpu
openai
tiktoken

# API & UI
fastapi
uvicorn
gradio

# File Handling / PDF / Log Parsing
unstructured
pymupdf

# LLM Inference (Local)
ollama

# For GitHub + CI Integration
pygithub

# AMD GPU / ROCm (optional for testing on AMD systems)
torch  # Use with ROCm build if running on AMD GPU

# Dev Tools
python-dotenv
httpx
requests
pip install torch --index-url https://download.pytorch.org/whl/rocm5.4.2
