from pydantic import BaseModel
from typing import List

class ReviewerOutput(BaseModel):
    status: str
    feedback: List[str]
