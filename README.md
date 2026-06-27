# 🚀 AI App Compiler

## Overview

AI App Compiler converts natural language requirements into a structured, validated and executable software blueprint.

Example Input:

> Build a CRM with login, contacts, dashboard, role-based access and premium plans.

Generated Output:

* Intent Specification
* System Architecture
* Database Schema
* API Schema
* UI Schema
* Authentication Rules
* Validation Report
* Repaired Schema
* FastAPI Runtime Code
* SQL Schema

---

## Compiler Pipeline

```text
┌─────────────────────────┐
│      User Prompt        │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│   Intent Extraction     │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│     System Design       │
│ (Entities, Roles, Flow) │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│   Schema Generation     │
├─────────────────────────┤
│ • Database Schema       │
│ • API Schema            │
│ • UI Schema             │
│ • Auth Rules            │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│    Validation Engine    │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│      Repair Engine      │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│   Runtime Generation    │
├─────────────────────────┤
│ • FastAPI Code          │
│ • SQL Schema            │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│  Executable App Output  │
└─────────────────────────┘
```

---

## Features

### Multi-Stage Generation Pipeline

* Intent Extraction
* System Design Layer
* Schema Generation
* UI Generation
* Authentication Generation
* Validation Engine
* Repair Engine
* Runtime Generation

### Reliability Features

✅ Structured JSON Output

✅ Schema Validation

✅ Automatic Repair Engine

✅ Ambiguity Detection

✅ Clarification Handling

✅ Runtime Code Generation

✅ Evaluation Framework

✅ Edge Case Testing

---

## Ambiguity Handling

Example Input:

```text
Build something useful
```

Output:

```json
{
  "status": "clarification_required",
  "questions": [
    "What type of application do you want?",
    "Who are the users?",
    "What are the core features?",
    "Do you need authentication and roles?"
  ]
}
```

---

## Evaluation Framework

Dataset:

* 10 Real Product Prompts
* 10 Edge Case Prompts

Metrics Tracked:

* Success Rate
* Average Latency
* Repair Trigger Rate
* Failure Types
* Clarification Requests

Files:

```text
evaluation/
├── prompts.json
├── results.json
└── README.md
```

---

## Tech Stack

### Backend

* Python
* FastAPI

### Frontend

* React
* Axios
* Vite

### LLM

* Groq
* Llama 3.3 70B Versatile

---

## Project Structure

```text
backend/
├── pipeline/
│   ├── intent_extractor.py
│   ├── system_designer.py
│   ├── schema_generator.py
│   ├── ui_generator.py
│   ├── auth_generator.py
│   ├── validator.py
│   ├── repair_engine.py
│   ├── runtime_generator.py
│   ├── clarifier.py
│   └── llm.py
│
├── evaluation/
│
├── schemas/
│
├── frontend/
│
└── main.py
```

---

## Run Backend

```bash
uvicorn main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

---

## Run Frontend

```bash
npm install

npm run dev
```

Open:

```text
http://localhost:5173
```

---

## Sample Prompt

```text
Build a CRM with login, contacts, dashboard, role-based access, premium subscription plans and admin analytics.
```

---

## Author

Shivaleela A Ballary

Computer Science Engineering

AI App Compiler 
