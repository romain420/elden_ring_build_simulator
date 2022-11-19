from sqlite3 import Date
from sqlalchemy import Column, String, DateTime, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.schema import Identity
from database import BaseSQL
from sqlalchemy.orm import relationship
from sqlalchemy.types import ARRAY
from MutableList import MutableList


#Creation de toute les tables de la db

#table user
class User(BaseSQL):
    __tablename__ = "users"

    id =            Column(Integer, primary_key=True) #auto-increment
    username =      Column(String, nullable=False, unique=True)
    First_name =    Column(String, nullable=False)
    Last_name =     Column(String, nullable=False)
    age =           Column(Integer, nullable=False)
    email =         Column(String, nullable=False)
    password  =     Column(String, nullable=False)
    created_at =    Column(DateTime, nullable=False)
    last_visit =    Column(DateTime, nullable=False)
    nb_builds =     Column(Integer, nullable=False)
    builds =        Column(MutableList.as_mutable(ARRAY(String)), nullable=False)       # Les updates de liste python n'envoie pas d'update lors de la modification, nous transformons donc notre ARRAY en mutable 
                                                                                        # personnalisée qui renverrat des updates lors des changements. Voir MutableList.py pour la structure de la classe. 
    
    #build = relationship("User_build", back_populates="owner")

#table user_build
class User_build(BaseSQL):
    __tablename__ = "user_builds"

    id =                Column(Integer, primary_key=True) #auto-increment
    name =              Column(String, nullable = False)          # a changer plus tard, pas sur de savoir comment ajouter une classe custom
    created_at =        Column(DateTime, nullable = False)
    last_visit =        Column(DateTime, nullable = False)
    last_update =       Column(DateTime, nullable = False)        # devrait-on sauvegarder les précédentes versions des builds ? ou useless ?
    nb_visits =         Column(Integer, nullable = False)
    nb_items =          Column(Integer, nullable = False) 
    items_id =          Column(String, nullable=False)
    owner_username =    Column(String, ForeignKey("users.username"))
    
    #owner = relationship("User", back_populates="build")
    #item = relationship("Item", back_populates="stuff")

#table item
class Item(BaseSQL):
    __tablename__ = "items"

    id =            Column(Integer, primary_key=True) #auto-increment
    name =          Column(String, nullable = False, unique=True)
    image =         Column(String, nullable = False)
    description =   Column(String, nullable = False)
    category =      Column(String, nullable = False)
    dmg_negation =  Column(String, nullable = False)    # encore une fois pas sur, surement un Enum of Dictionnaires  le format est: ...{name: "Phy", amount: 7}, {name: "Strike", amount: 6},...
    resistance =    Column(String, nullable = False)    # pareil qu'au dessus
    weight =        Column(Integer, nullable = False)
    
    #stuff = relationship("User_build", back_populates="item")


# #table build
# class Build(BaseSQL):
#     __tablename__= "builds"

#     id =            Column(String, primary_key=True, index=True)
#     elmet :         Column(String)
#     gantlet :       Column(String)
#     choose :        Column(String)
#     weapon :        Column(String)


