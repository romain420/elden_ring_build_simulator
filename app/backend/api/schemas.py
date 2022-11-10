from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from uuid import uuid4
from typing_extensions import Annotated

#schema in database of all differents table

#schema class User
class User(BaseModel):
    id : Annotated[str, Field(default_factory=lambda: uuid4().hex)]#str
    username :          str
    First_name :        str
    Last_name :         str
    date_of_birth :     datetime
    email :             str    
    password:           str
    created_at :        datetime
    last_visit :        datetime
    nb_builds :         int
    builds :            list

    class Config:
        orm_mode = True


#schema class User_build
class User_build(BaseModel):
    # __tablename__ = "user_builds"

    id :            Annotated[str, Field(default_factory=lambda: uuid4().hex)]#str
    name :          str
    owner :         User
    created_at :    datetime
    last_visit :    datetime
    last_update :   datetime
    nb_visits :     int
    items :         list
    nb_items :      int

    class Config:
        orm_mode = True


#schema class Item
class Item(BaseModel):

    id :            Annotated[str, Field(default_factory=lambda: uuid4().hex)]#str
    name :          str
    image :         str
    description :   str
    category :      str
    dmg_negation :  list
    resistance :    list
    weight :        int

    class Config:
        orm_mode = True

#-------------------------------------------------------------------------#

#schema class Build
# class Build(BaseModel):
#     id : str#Annotated[str, Field(default_factory=lambda: uuid4().hex)]
#     elmet : str
#     Last_name : str
#     gantlet : str
#     choose : str
#     weapon : str

#     class Config:
#         orm_mode = True