from pydantic import BaseModel

class Todo(BaseModel):
    priority: int
    description: str