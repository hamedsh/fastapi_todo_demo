from typing import List

from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session

import fastapi_todo.crud.todo_crud as todo_crud
from fastapi_todo.crud.user_crud import get_current_user
from fastapi_todo.db import get_db
from fastapi_todo.models import UserModel
from fastapi_todo.schemas.todo_schemas import TodoSchema, TodoBaseSchema, TodoUpdateSchema, TodoResponseSchema

todo_router = APIRouter()


@todo_router.get('', response_model=List[TodoResponseSchema])
def get_my_todos_view(db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    todos = todo_crud.get_user_todos(db, current_user)
    return todos


@todo_router.post('', response_model=List[TodoResponseSchema])
def add_todo_view(
        todo_data: TodoBaseSchema,
        db: Session = Depends(get_db),
        current_user: UserModel = Depends(get_current_user),
):
    todo_crud.add_todo(
        db,
        current_user,
        todo_data,
    )
    todos = todo_crud.get_user_todos(db, current_user)
    return todos


@todo_router.put('', response_model=List[TodoResponseSchema])
def update_todo_view(
        todo_data: TodoUpdateSchema,
        db: Session = Depends(get_db),
        current_user: UserModel = Depends(get_current_user),
):
    todo_crud.update_todo(
        db,
        new_todo=todo_data,
    )
    todos = todo_crud.get_user_todos(db, current_user)
    return todos


@todo_router.delete('/{todo_id:int}', response_model=List[TodoResponseSchema])
def delete_todo_view(
        todo_id: int,
        db: Session = Depends(get_db),
        current_user: UserModel = Depends(get_current_user)
):
    todo_crud.delete_todo(db, todo_id)
    todos = todo_crud.get_user_todos(db, current_user)
    return todos
