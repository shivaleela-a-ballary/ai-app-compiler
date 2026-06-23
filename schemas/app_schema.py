from pydantic import BaseModel
from typing import List


class Entity(BaseModel):
    name: str
    fields: List[str]


class APIEndpoint(BaseModel):
    path: str
    method: str


class AppConfig(BaseModel):
    app_type: str
    entities: List[Entity]
    apis: List[APIEndpoint]