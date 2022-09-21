from sqlalchemy import Column, String, DateTime, Float, Integer
from sqlalchemy.dialects.postgresql import UUID
from database import BaseSQL

#Creation de toute les tables de la db

#table user
class User(BaseSQL):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True)#Column(UUID(as_uuid=True), primary_key=True, index=True)
    First_name = Column(String)
    Last_name = Column(String)
    date_of_birth = Column(DateTime)
    email = Column(String)


#table build
class Build(BaseSQL):
    __tablename__= "builds"

    id = Column(String, primary_key=True, index=True)
    elmet : Column(String)
    gantlet : Column(String)
    choose : Column(String)
    weapon : Column(String)


