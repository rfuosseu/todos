from fastapi import APIRouter, HTTPException
from typing import List
from todo import Todo, TodoCreate
from database import todos, next_id
from datetime import datetime

router = APIRouter(
    prefix="/todos",
    tags=["todos"],
)


# TODO: Implémenter la route GET /todos
# - Retourner la liste complète des todos
# - Type de retour : List[Todo]
@router.get("/", response_model=List[Todo])
def get_todos():
    return todos


# TODO: Implémenter la route POST /todos
# - Recevoir un TodoCreate dans le body
# - Générer un id avec next_id()
# - Définir created_at avec datetime.now()
# - Ajouter le todo à la liste
# - Retourner le todo créé avec le status code 201
@router.post("/", response_model=Todo, status_code=201)
def create_todo(todo: TodoCreate):
    new_todo = Todo(
        id=next_id(),
        title=todo.title,
        description=todo.description,
        completed=False,
        created_at=datetime.now(),
    )
    todos.append(new_todo)
    return new_todo

# TODO: Implémenter la route PUT /todos/{id}
# - Recevoir un TodoCreate dans le body
# - Trouver le todo correspondant à l'id
# - Mettre à jour le titre et la description
# - Retourner le todo mis à jour
# - Si le todo n'existe pas, retourner une erreur 404
@router.put("/{id}", response_model=Todo)
def update_todo(id: int, todo: TodoCreate):
    for t in todos:
        if t.id == id:
            t.title = todo.title
            t.description = todo.description
            return t
    raise HTTPException(status_code=404, detail="Todo not found")