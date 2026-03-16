from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None


class TodoCreate(TodoBase):
    # TODO: Ajouter les champs nécessaires à la création d'un todo
    pass


class Todo(TodoBase):
    id: int
    completed: bool = False
    created_at: datetime

    class Config:
        from_attributes = True
