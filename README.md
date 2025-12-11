# 🌸 Scene2Manga-AI  
### _Transforming written scenes into stunning manga-style illustrations using LLaMA 3, LangChain, and SDXL Diffusion_

---

## 📖 Overview

**Scene2Manga-AI** is a multimodal Generative AI system that converts simple natural-language scene descriptions into **high-quality manga panels**.  
It combines the reasoning power of **LLaMA 3**, the orchestration capability of **LangChain**, and the artistic strength of **Animagine XL (SDXL Diffusion)** to create automated manga illustrations with professional-level detailing.

---

## ✨ Why This Project Exists

Most AI image generators struggle with:

| Problem in Existing Solutions | How Scene2Manga-AI Fixes It |
|------------------------------|-----------------------------|
| Inconsistent style | Uses SDXL Animagine XL for clean, consistent manga lineart |
| Poor scene understanding | LLaMA 3 expands user scenes into detailed prompts |
| Weak manga aesthetics | Adds screentones, composition, lighting cues |
| Dependence on user prompt skill | Fully automated prompt engineering |
| No end-to-end automation | LangChain agent orchestrates tools intelligently |

---

## 🌟 What Makes Scene2Manga-AI Better

### ✔ Deep scene understanding through LLaMA 3  
Your simple sentence becomes a cinematic, manga-specific description.

### ✔ True agentic workflow  
A LangChain agent decides how to route input and which tools to execute.

### ✔ Superior manga rendering  
Built on Animagine XL → sharper lineart, better screentones, professional look.

### ✔ Fully local & open-source  
No paid APIs, no cloud dependencies.

---

## 🏗 Internal Architecture
```
              ┌────────────────────────────┐
              │        User Input          │
              │  "A samurai under moonlight"│
              └──────────────┬─────────────┘
                             │
                             ▼
                 ┌─────────────────────┐
                 │   LLaMA 3 (Ollama)  │
                 │  Scene Expansion    │
                 └─────────────────────┘
                             │
            Generates manga-optimized prompt
                             │
                             ▼
               ┌──────────────────────────┐
               │    LangChain Agent       │
               │  Tool Orchestration      │
               └──────────────────────────┘
                       │            │
                       │            │
      ┌────────────────┘            └──────────────────┐
      ▼                                                ▼
┌────────────────────┐ ┌──────────────────────┐
│ expand_prompt Tool │ │ generate_manga Tool │
│ (LLM-based logic) │ │ (SDXL Diffusion) │
└────────────────────┘ └──────────────────────┘
│
▼
┌─────────────────────┐
│ Final Image │
│ (Base64 PNG Manga) │
└─────────────────────┘
```


---
```
## 🔍 Key Components

| Component | Role |
|-----------|------|
| **LLaMA 3 (Ollama)** | Expands text into detailed manga prompts |
| **LangChain Tools** | Define prompt expansion + diffusion generation |
| **LangChain Agent** | Controls execution order intelligently |
| **Animagine XL (SDXL)** | Generates manga-style images |
| **FastAPI Backend** | Exposes the entire system as a REST API |

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| Natural-language → Manga | Converts descriptions into illustrated manga scenes |
| Auto Prompt Engineering | Uses LLaMA to create cinematic prompts |
| High-Resolution Output | Generates 1024×1024 manga panels |
| Agentic Workflow | LangChain orchestrates multi-step reasoning |
| Fully Local | No external APIs required |
| Modular Architecture | Easy to extend with LoRAs, new tools, etc. |

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/generate` | Generate manga image from scene text |
| GET | `/health` | Health check |
```
---

## 📦 Request & Response Example

### **POST** `/api/generate`

#### Request:
```json
{
  "scene_text": "A samurai standing under the moonlight"
}
Response:
json
Copy code
{
  "expanded_prompt": "... final prompt ...",
  "image_base64": "iVBORw0KGgoAAAANSUhEUgAAA..."
}
🏗 Folder Structure
arduino
Copy code
backend/
└── app/
    ├── models/        → LLaMA + Diffusion engines
    ├── langchain/     → Tools + agent
    ├── services/      → Pipeline logic
    ├── routes/        → API endpoints
    ├── main.py        → FastAPI entry point
