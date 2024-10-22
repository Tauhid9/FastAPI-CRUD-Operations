from typing import  Optional
from pydantic import BaseModel, Field

class BookSchema(BaseModel):
    id: Optional[int]=None
    name: Optional[str]=None
    description: Optional[str]=None

    class Database:
        orm_mode=True

class RequestBook(BaseModel):
    parameter: BookSchema=Field(...)


