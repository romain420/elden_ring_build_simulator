from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from uuid import uuid4
from typing_extensions import Annotated

#schema in database of all differents table

#schema class User
class User(BaseModel):
    id : str#Annotated[str, Field(default_factory=lambda: uuid4().hex)]
    First_name : str
    Last_name : str
    date_of_birth : datetime
    # start_date : datetime
    email : str

    class Config:
        orm_mode = True

#schema class Build
class Build(BaseModel):
    id : str#Annotated[str, Field(default_factory=lambda: uuid4().hex)]
    elmet : str
    Last_name : str
    gantlet : str
    choose : str
    weapon : str

    class Config:
        orm_mode = True