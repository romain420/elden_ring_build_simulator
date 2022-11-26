from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from uuid import uuid4
from typing_extensions import Annotated

#schema in database of all differents table
#schema class User
class User(BaseModel):
    username :          str
    First_name :        str
    Last_name :         str
    age :               int
    email :             str    
    password:           str

    class Config:
        orm_mode = True


#schema class User_build
class User_build(BaseModel):

    name :              str
    created_at :        datetime
    last_visit :        datetime
    last_update :       datetime
    nb_visits :         int
    nb_items :          int
    items_id :          list
    owner_username :    str


    class Config:
        orm_mode = True


#schema class Item
class Item(BaseModel):

    name :          str
    image :         str
    description :   str
    category :      str
    dmg_negation :  list
    resistance :    list
    weight :        int

    class Config:
        orm_mode = True


#schema class Stat
class Stat(BaseModel):

    vigor:          int
    mind:           int
    endurance:      int
    strength:       int
    dexterity:      int
    intelligence:   int
    faith:          int
    arcane:         int

    class Config:
        orm_mode = True


#schema class CharacUser
class CharacStats(BaseModel):

    runeLevel :         int
    HP :                int
    FP :                int
    stamina :           int
    equipLoad :         int
    physicalDefense :   int
    magicDefense :      int
    fireDefense :       int
    lightningDefense :  int
    holyDefense :       int
    immunity :          int
    robustness   :      int
    focus :             int
    vitality :          int

    class Config:
        orm_mode = True