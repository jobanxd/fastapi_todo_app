from pydantic import BaseModel

class Todo(BaseModel):
    id: int
    task: str
    done: bool = False

