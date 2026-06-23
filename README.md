# AI App Compiler

## Overview

AI App Compiler converts a natural language application idea into a complete software blueprint.

Example:

> Build a CRM with login, contacts, dashboard and admin role

The system automatically generates:

* Application intent
* Architecture design
* Database schema
* API schema
* UI schema
* Role-based access control
* Validation & repair
* FastAPI code
* SQL schema

---

## Architecture

User Prompt
↓
Intent Extractor (Groq)
↓
System Designer
↓
Schema Generator
↓
UI Generator
↓
Auth Generator
↓
Validation Engine
↓
Repair Engine
↓
Runtime Generator
├── FastAPI Code
└── SQL Code

---

## Tech Stack

* Python
* FastAPI
* Groq API
* Llama 3.3 70B
* JSON Schema

---

## Run Locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Open:

http://127.0.0.1:8000/docs

---

## Sample Prompt

Build a CRM with login and contacts

---

## Output

* Intent
* Architecture
* Database Schema
* API Schema
* UI Schema
* Authentication Rules
* Generated FastAPI Code
* Generated SQL Code
