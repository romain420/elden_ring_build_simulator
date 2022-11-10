from sqlite3 import Date
from sqlalchemy import Column, String, DateTime, Float, Integer, Enum, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from database import BaseSQL
from sqlalchemy.orm import relationship


#Creation de toute les tables de la db

#table user
class User(BaseSQL):
    __tablename__ = "users"

    id =            Column(UUID(as_uuid=True), primary_key=True, index=True)#Column(String, primary_key=True, index=True)
    username =      Column(String, nullable = False)
    First_name =    Column(String, nullable = False)
    Last_name =     Column(String, nullable = False)
    date_of_birth = Column(DateTime, nullable = False)
    email =         Column(String, nullable=False)#TODO manage the fact that user can't have a the same email as an other one in frontend part
    password  =     Column(String, nullable = False)
    created_at =    Column(DateTime, nullable = False)
    last_visit =    Column(DateTime, nullable = False)
    nb_builds =     Column(Integer, nullable = False)
    builds =        Column(String, nullable = False)        # not sure about this  but Enum of User_build, on ne peut pas mettre de classes custom pour l'instant.
    
    build = relationship("User_build", back_populates="owner")

#table user_build
class User_build(BaseSQL):
    __tablename__ = "user_builds"

    id =            Column(UUID(as_uuid=True), primary_key=True, index=True)#Column(String, primary_key=True, index=True)
    name =          Column(String, nullable = False)          # a changer plus tard, pas sur de savoir comment ajouter une classe custom
    created_at =    Column(DateTime, nullable = False)
    last_visit =    Column(DateTime, nullable = False)
    last_update =   Column(DateTime, nullable = False)        # devrait-on sauvegarder les précédentes versions des builds ? ou useless ?
    nb_visits =     Column(Integer, nullable = False)
    nb_items =      Column(Integer, nullable = False) 
    items_id =      Column(UUID(as_uuid=True), ForeignKey("items.id"))    # pareil jsuis pas sur mais surement un Enum of Item, peut pas mettre de classe custom pour l'instant
    owner_id =      Column(UUID(as_uuid=True), ForeignKey("users.id"))        # revient a dire items.size
    
    owner = relationship("User", back_populates="build")
    item = relationship("Item", back_populates="stuff")

#table item
class Item(BaseSQL):
    __tablename__ = "items"

    id =            Column(UUID(as_uuid=True), primary_key=True, index=True)#Column(String, primary_key=True, index=True)
    name =          Column(String, nullable = False)
    image =         Column(String, nullable = False)
    description =   Column(String, nullable = False)
    category =      Column(String, nullable = False)
    dmg_negation =  Column(String, nullable = False)    # encore une fois pas sur, surement un Enum of Dictionnaires  le format est: ...{name: "Phy", amount: 7}, {name: "Strike", amount: 6},...
    resistance =    Column(String, nullable = False)    # pareil qu'au dessus
    weight =        Column(Integer, nullable = False)
    
    stuff = relationship("User_build", back_populates="item")


# #table build
# class Build(BaseSQL):
#     __tablename__= "builds"

#     id =            Column(String, primary_key=True, index=True)
#     elmet :         Column(String)
#     gantlet :       Column(String)
#     choose :        Column(String)
#     weapon :        Column(String)

