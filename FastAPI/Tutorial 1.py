from fastapi import FastAPI

api = FastAPI()

all_todos = [
    {'todo_id': 1, 'todo_name': 'Sports', 'todo_description': 'Go to the gym'},
    {'todo_id': 2, 'todo_name': 'Read', 'todo_description': 'Read 10 pages'},
    {'todo_id': 3, 'todo_name': 'Shop', 'todo_description': 'Buy this book'},
    {'todo_id': 4, 'todo_name': 'Study', 'todo_description': 'Learn FastAPI'},
    {'todo_id': 5, 'todo_name': 'Meditate', 'todo_description': '10 mins of meditation'}
]

# GET, POST, PUT, DELETE

@api.get('/')
def index():
    return {'message': 'Hello, World!'}

@api.get('/calculation')
async def get_data_from_db():
    pass
    # await response

@api.get('/todos/{todo_id}')
def get_todo(todo_id: int):
    for todo in all_todos:
        if todo['todo_id'] == todo_id:
            return todo
    return {'message': 'Todo not found'}

# first_n can be used with:
# http://127.0.0.1:5000/todos?first_n=3
@api.get('/todos')
def get_todos(first_n: int = None):
    if first_n:
        return all_todos[:first_n]
    return all_todos

@api.post('/todos')
def add_todo(todo: dict):
    new_todo_id = max(todo['todo_id'] for todo in all_todos) + 1
    todo['todo_id'] = new_todo_id
    all_todos.append(todo)
    return {'message': 'Todo added successfully'}

@api.put('/todos')
def update_todo(todo_id: int, updated_todo: dict):
    for todo in all_todos:
        if todo['todo_id'] == todo_id:
            if updated_todo.get('todo_name'):
                todo['todo_name'] = updated_todo['todo_name']
            if updated_todo.get('todo_description'):
                todo['todo_description'] = updated_todo['todo_description']
            return {"message": "Todo updated successfully."}
    return {"message": "Todo ID not found."}

@api.delete('/todos')
def delete_todos(todo_id: int):
    for ind, todo in enumerate(all_todos):
        if todo['todo_id'] == todo_id:
            all_todos.pop(ind)
            return {"message": "Todo ID deleted successfully."}
    return {"message": "Todo ID not found."}