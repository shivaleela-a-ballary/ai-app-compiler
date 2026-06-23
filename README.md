# AI App Compiler

## Overview

AI App Compiler converts natural language application requirements into a structured, validated, executable software blueprint.

Example Input:

> Build a CRM with login, contacts, dashboard and admin role

The system generates:

* Intent Specification
* Application Architecture
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

User Prompt
↓
Intent Extraction
↓
System Design
↓
Schema Generation
↓
UI Generation
↓
Authentication Generation
↓
Validation Engine
↓
Repair Engine
↓
Runtime Generator
├── FastAPI Code
└── SQL Code

---

## Features

### Multi-Stage Generation Pipeline

* Intent Extraction
* System Design Layer
* Schema Generation
* Validation Layer
* Repair Layer
* Runtime Generation

### Reliability

* Structured JSON output
* Validation checks
* Automatic repair mechanism
* Cross-layer consistency checks

### Runtime Awareness

Generated outputs can be directly used for:

* FastAPI backend generation
* SQL schema generation

---

## Evaluation Framework

Dataset:

* 10 Real Product Prompts
* 10 Edge Case Prompts

Metrics:

* Success Rate
* Repair Trigger Rate
* Failure Types
* Average Latency

Results available in:

evaluation/results.json

---

## Tech Stack

Backend:

* Python
* FastAPI

LLM:

* Groq
* Llama 3.3 70B

Frontend:

* React
* Axios

---

## Run

Backend:

```bash
uvicorn main:app --reload
```

Frontend:

```bash
npm run dev
```

---

## Sample Prompt

Build a CRM with login and contacts

---

## Repository Structure

backend/
├── pipeline/
├── schemas/
├── evaluation/
└── main.py

frontend/

README.md
ARCHITECTURE.md
