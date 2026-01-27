from pydantic import BaseModel
from typing import List

class MCQ(BaseModel):
    question: str
    options: List[str]
    answer: str

class GeneratorOutput(BaseModel):
    explanation: str
    mcqs: List[MCQ]
