from fastapi import FastAPI
from routers.todos import todo_router

api = FastAPI()

api.include_router(todo_router)

# tags are used to put them in groups in fastAPI's docs.
@api.get('/', tags=['root'])
def index():
    return {'message': 'Hello, World!'}