from fastapi import FastAPI

from models import TodoModel

app = FastAPI()
todos = []

@app.get("/")
def read_root():
    return {"Hello": "World"}

# Get all todos
@app.get("/todos")
async def get_todos():
    return {"todos": todos}

# Get a single todo
@app.get("/todos/{todo_id}")
async def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return {"todo": todo}
    return {"Message": "No such todo"}

# Create a new todo
@app.post("/todos")
async def create_todo(todo: TodoModel):
    todos.append(todo)
    return {"Message": "Todo created successfully"}

# Update a todo
@app.put("/todos/{todo_id}")
async def update_todo(todo_id: int, new_todo: TodoModel):
    for todo in todos:
        if todo.id == todo_id:
            todo.id = new_todo.id
            todo.item = new_todo.item
            return {"Message": "Todo updated successfully"}
    return {"Message": "Todo not found"}

# Delete a todo
@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id : int):
    for todo in todos:
        if todo.id == todo_id:
            todos.remove(todo)
            return {"Message": "Todo deleted successfully"}
    return {"Message": "No such todo"}
