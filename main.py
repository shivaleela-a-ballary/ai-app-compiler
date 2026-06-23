from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pipeline.intent_extractor import extract_intent
from pipeline.system_designer import design_system
from pipeline.schema_generator import generate_schemas
from pipeline.ui_generator import generate_ui
from pipeline.auth_generator import generate_auth
from pipeline.validator import validate_schema
from pipeline.repair_engine import repair_schema
from pipeline.runtime_generator import (
    generate_fastapi_code,
    generate_sql_schema
)

from pipeline.clarifier import (
    needs_clarification,
    clarification_questions
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "AI App Compiler Running"
    }


@app.post("/generate")
def generate(prompt: str):

    # Ambiguity Handling
    if needs_clarification(prompt):
        return {
            "status": "clarification_required",
            "questions": clarification_questions()
        }

    print("STEP 1")
    intent = extract_intent(prompt)

    print("STEP 2")
    architecture = design_system(intent)

    print("STEP 3")
    schemas = generate_schemas(architecture)

    print("STEP 4")
    ui_schema = generate_ui(architecture)

    print("STEP 5")
    auth_schema = generate_auth(intent)

    print("STEP 6")
    validation = validate_schema(schemas)

    print("STEP 7")
    repaired = repair_schema(
        schemas,
        validation
    )

    print("STEP 8")
    api_code = generate_fastapi_code(schemas)

    sql_code = generate_sql_schema(schemas)

    return {
        "status": "success",
        "intent": intent,
        "architecture": architecture,
        "schemas": schemas,
        "ui": ui_schema,
        "auth": auth_schema,
        "validation": validation,
        "repaired": repaired,
        "generated_code": {
            "fastapi": api_code,
            "sql": sql_code
        }
    }