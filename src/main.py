from fastapi import FastAPI
from api.v1 import todo

app = FastAPI(title="ToDo API", version="1.0")

# Register Routers
app.include_router(todo.router)