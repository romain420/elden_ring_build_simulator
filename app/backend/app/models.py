from sqlite3 import Date
from sqlalchemy import Column, String, DateTime, Float, Integer, Enum
from sqlalchemy.dialects.postgresql import UUID
from database import BaseSQL


#Creation de toute les tables de la db

#table user
class User(BaseSQL):
    __tablename__ = "users"

    id =            Column(String, primary_key=True, index=True)   #Column(UUID(as_uuid=True), primary_key=True, index=True)
    First_name =    Column(String)
    Last_name =     Column(String)
    date_of_birth = Column(DateTime)
    email =         Column(String)
    password  =     Column(String)
    created_at =    Column(DateTime)
    last_visit =    Column(DateTime)
    nb_builds =     Column(Integer)
    builds =        Column(Enum)        # not sure about this  but Enum of User_build

#table user_build
class User_build(BaseSQL):
    __tablename__ = "user_builds"

    id =            Column(String, primary_key=True, index=True)
    name =          Column(String)
    owner =         Column(User)
    created_at =    Column(DateTime)
    last_visit =    Column(DateTime)
    last_update =   Column(DateTime)    # devrait-on sauvegarder les précédentes versions des builds ? ou useless ?
    nb_visits =     Column(Integer)
    items =         Column(Enum)        # pareil jsuis pas sur mais surement un Enum of Item
    nb_items =      Column(Integer)     # revient a dire items.size

#table item
class Item(BaseSQL):
    __tablename__ = "items"

    id =            Column(String, primary_key=True, index=True)
    name =          Column(String)
    image =         Column(String)
    description =   Column(String)
    category =      Column(String)
    dmg_negation =  Column(Enum)        # encore une fois pas sur, surement un Enum of Dictionnaires  le format est: ...{name: "Phy", amount: 7}, {name: "Strike", amount: 6},...
    resistance =    Column(Enum)    # pareil qu'au dessus
    weight =        Column(Integer)


#table build
class Build(BaseSQL):
    __tablename__= "builds"

    id =            Column(String, primary_key=True, index=True)
    elmet :         Column(String)
    gantlet :       Column(String)
    choose :        Column(String)
    weapon :        Column(String)


