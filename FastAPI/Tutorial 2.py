from enum import IntEnum
from typing import List, Optional
from pydantic import BaseModel, Field
from fastapi import FastAPI, HTTPException

api = FastAPI()

all_todos = [
    {'todo_id': 1, 'todo_name': 'Sports', 'todo_description': 'Go to the gym'},
    {'todo_id': 2, 'todo_name': 'Read', 'todo_description': 'Read 10 pages'},
    {'todo_id': 3, 'todo_name': 'Shop', 'todo_description': 'Buy this book'},
    {'todo_id': 4, 'todo_name': 'Study', 'todo_description': 'Learn FastAPI'},
    {'todo_id': 5, 'todo_name': 'Meditate', 'todo_description': '10 mins of meditation'}
]

class Priority(IntEnum):
    LOW = 3
    MEDIUM = 2
    HIGH = 1

class TodoBase(BaseModel):
    todo_name: str = Field(..., min_length = 3, max_length = 512, description = 'Name of the todo')
    todo_description: str = Field(..., description = 'Description of the todo')
    priority: Priority = Field(default=Priority.LOW, description = 'Priority of the todo')

class TodoCreate(TodoBase):
    pass

class Todo(TodoBase):
    todo_id: int = Field(..., description = 'Unique Identifier of a todo.')

class TodoUpdate(BaseModel):
    todo_name: Optional[str] = Field(default = None, min_length = 3, max_length = 512, description = 'Name of the todo')
    todo_description: Optional[str] = Field(default = None, description = 'Description of the todo')
    priority: Optional[Priority] = Field(None, description = 'Priority of the todo')

# all_todos converted to Todo object
all_todos = [Todo(**todo) for todo in all_todos]

@api.get('/todos/{todo_id}', response_model=Todo)
def get_todo(todo_id: int):
    for todo in all_todos:
        if todo.todo_id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

# first_n can be used with:
# http://127.0.0.1:5000/todos?first_n=3
@api.get('/todos', response_model=List[Todo])
def get_todos(first_n: int = 0):
    if first_n:
        return all_todos[:first_n]
    return all_todos

@api.post('/todos', response_model=Todo)
def add_todo(todo: TodoCreate):
    new_todo_id = max([t.todo_id for t in all_todos] + [0]) + 1
    new_todo = Todo(
        todo_id=new_todo_id,
        todo_name=todo.todo_name,
        todo_description=todo.todo_description,
        priority=todo.priority
    )
    all_todos.append(new_todo)
    return new_todo

@api.put('/todos/{todo_id}', response_model=Todo)
def update_todo(todo_id: int, updated_todo: TodoUpdate):
    for todo in all_todos:
        if todo.todo_id == todo_id:
            if updated_todo.todo_name:
                todo.todo_name = updated_todo.todo_name
            if updated_todo.todo_description:
                todo.todo_description = updated_todo.todo_description
            if updated_todo.priority:
                todo.priority = updated_todo.priority
            return todo
    raise HTTPException(status_code=404, detail="Todo ID not found")

@api.delete('/todos/{todo_id}', response_model=Todo)
def delete_todos(todo_id: int):
    for ind, todo in enumerate(all_todos):
        if todo.todo_id == todo_id:
            all_todos.pop(ind)
            return todo
    raise HTTPException(status_code=404, detail="Todo ID not found")