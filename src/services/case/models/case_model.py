from pydantic import BaseModel
from pydantic.types import List
from src.services.case.models.priority import Priority


class Case(BaseModel):
    id: int
    name: str
    description: str
    steps: List[str]
    expected_result: str
    priority: Priority
