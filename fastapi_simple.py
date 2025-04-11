from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

app = FastAPI(title="Simple fastapi tutorial")

@app.get("/") #path
def hello_world():
    return {"message": "hello world"}

@app.get("/hello/{name}") #path
def hello_name(name: str):
    return{"message": f"hello {name}"}

class Todo(BaseModel):
    title:str
    completed:bool = False

todos = []

@app.get("/todos")
def get_todos():
    return todos

@app.post("/todos")
def create_todo(todo: Todo):
    todos.append(todo)
    return {"message": "todo created", "todo":todo}

@app.get("/todos/{todo_id}")
def get_todo(todo_id:int):
    if todo_id < 0 or todo_id >= len(todos):
        return {"message": "todo not found"}
    return todos[todo_id]

@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, todo: Todo):
    if todo_id < 0 or todo_id >= len(todos):
        return {"message": "todo not found"}
    todos[todo_id] = todo
    return {"message": "todo updated", "todo":todo}

if __name__ == "__main__":
    uvicorn.run("fastapi_simple:app" , host="0.0.0.0", port=8000, reload=True)