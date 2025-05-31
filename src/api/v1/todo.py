from fastapi import APIRouter, HTTPException
from models.todo import Todo
from services import todo_service


router = APIRouter(prefix="/todos")

@router.post("/")
def create_todos(todo: Todo):
    return todo_service.create_todo(todo)

@router.get("/")
def get_todos():
    return todo_service.get_all_todos()

@router.get("/{todo_id}")
def get_todo_by_id(todo_id: int):
    todo = todo_service.get_todo_by_id(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found!")
    return todo


