from models.todo import Todo
from typing import List, Optional

# In memory store only
todos: List[Todo] = []

def create_todo(todo: Todo) -> Todo:
    todos.append(todo)
    return todo

def get_all_todos() -> List[Todo]:
    return todos

def get_todo_by_id(todo_id: int) -> Optional[Todo]:
    return next((todo for todo in todos if todo.id == todo_id),None)
    