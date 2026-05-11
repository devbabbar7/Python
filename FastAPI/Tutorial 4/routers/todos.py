from fastapi import APIRouter

todo_router = APIRouter(prefix="/todos", tags=["todos"])

all_todos = [
    {'todo_id': 1, 'todo_name': 'Sports', 'todo_description': 'Go to the gym'},
    {'todo_id': 2, 'todo_name': 'Read', 'todo_description': 'Read 10 pages'},
    {'todo_id': 3, 'todo_name': 'Shop', 'todo_description': 'Buy this book'},
    {'todo_id': 4, 'todo_name': 'Study', 'todo_description': 'Learn FastAPI'},
    {'todo_id': 5, 'todo_name': 'Meditate', 'todo_description': '10 mins of meditation'}
]

# GET single todo
@todo_router.get('/{todo_id}')
def get_todo(todo_id: int):
    for todo in all_todos:
        if todo['todo_id'] == todo_id:
            return todo
    return {'message': 'Todo not found'}

# GET all todos
@todo_router.get('/')
def get_todos(first_n: int = None):
    if first_n:
        return all_todos[:first_n]
    return all_todos

# POST todo
@todo_router.post('/')
def add_todo(todo: dict):
    new_todo_id = max(t['todo_id'] for t in all_todos) + 1
    todo['todo_id'] = new_todo_id

    all_todos.append(todo)

    return {'message': 'Todo added successfully'}

# PUT todo
@todo_router.put('/{todo_id}')
def update_todo(todo_id: int, updated_todo: dict):
    for todo in all_todos:
        if todo['todo_id'] == todo_id:

            if updated_todo.get('todo_name'):
                todo['todo_name'] = updated_todo['todo_name']

            if updated_todo.get('todo_description'):
                todo['todo_description'] = updated_todo['todo_description']

            return {"message": "Todo updated successfully."}

    return {"message": "Todo ID not found."}

# DELETE todo
@todo_router.delete('/{todo_id}')
def delete_todo(todo_id: int):
    for ind, todo in enumerate(all_todos):

        if todo['todo_id'] == todo_id:
            all_todos.pop(ind)

            return {"message": "Todo deleted successfully."}

    return {"message": "Todo ID not found."}