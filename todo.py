from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class TodoBase(BaseModel):
    title: str
    description: str | None = None


class TodoCreate(TodoBase):
    # TODO: Ajouter les champs nécessaires à la création d'un todo
    pass


class TodoUpdate(BaseModel):
    title: str | None = None
    description: str | None = None


class Todo(TodoBase):
    id: int
    completed: bool = False
    created_at: datetime

    class Config:
        from_attributes = True
