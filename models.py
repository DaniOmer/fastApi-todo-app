from pydantic import BaseModel

class TodoModel(BaseModel):
    id: int
    item: str