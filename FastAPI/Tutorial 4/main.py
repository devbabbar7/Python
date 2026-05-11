from fastapi import FastAPI
from routers.todos import todo_router

api = FastAPI()

api.include_router(todo_router)

@api.get('/')
def index():
    return {'message': 'Hello, World!'}