from pydantic import BaseModel


class TodoBaseSchema(BaseModel):
    text: str
    completed: bool


class TodoSchema(TodoBaseSchema):
    owner_id: int

    class Config:
        orm_mode = True


class TodoResponseSchema(TodoSchema):
    id: int


class TodoUpdateSchema(TodoBaseSchema):
    id: int


