from pydantic import BaseModel

class ContentInput(BaseModel):
    grade: int
    topic: str
