# from pydantic import BaseModel, Field
# from uuid import uuid4
# from typing_extensions import Annotated
import schemas, models, services
from database import engine, SessionLocal
from fastapi import Depends, FastAPI, HTTPException
from datetime import datetime
from sqlalchemy.orm import Session
from typing import Optional, List


models.BaseSQL.metadata.create_all(bind=engine)


app = FastAPI(
    title="My title",
    description="My description",
    version="0.0.1",
)

db = SessionLocal()

@app.get("/")
def read_root():
    return "Hello et bienvenue sur ce simulateur de build Elden Ring"


@app.get("/date")
def get_date():
    current_date = datetime.today()
    return f"On est actuellement le {current_date}"


# @app.on_event("startup")
# async def startup_event():
#     models.BaseSQL.metadata.create_all(bind=engine)


# @app.get("/base_test")
# async def base_get():
#     BaseSQL.metadata.create_all(bind=engine)



#--------------------------user API part--------------------------#

#-------------GET PART-------------#
@app.get("/users", status_code=200)
def get_all_users():
    all_users = services.get_users(db)
    return all_users

@app.get("/user_builds", status_code=200)
def get_all_user_builds():
    all_user_builds = services.get_user_builds(db)
    return all_user_builds

@app.get("/items", status_code=200)
def get_items():
    all_items = services.get_items(db)
    return all_items

@app.get("/users_summary", status_code=200)
def display_all_users():
    all_names = services.get_summary(db) 
    return all_names

@app.get("/display_users", status_code=200)
def display_all_users():
    all_names = services.get_summary(db) 
    return all_names

@app.get("/{username}", status_code=200)
def display_specific_user(username):
    user_infos = services.get_user_infos(db, username)
    return user_infos


#-------------POST PART-------------#
@app.post("/user")
async def post_user(user: schemas.User):
    services.create_user(db, user)

@app.post("/user_build")
async def post_user_build(user_build: schemas.User_build):
    services.create_user_build(db, user_build)

@app.post("/item")
async def post_item(item: schemas.Item):
    services.create_item(db, item)
   
#this API as to be avoid 
# @app.delete("/delete_user")
# async def remove_user(user:schemas.User):
#     deleted_user = services.delete_user_by_name(db, user)
    
#     return deleted_user


#-------------PUT PART-------------#
@app.put("/user_last_visit")#TODO don't forget to change the name by 'update_user_info'
async def update_last_visit(user:schemas.User):
    update_user = services.update_user_info(db, user)
    
    return update_user

@app.put("/delete_user")
async def delete_user(user:schemas.User):
    removed_user = services.kill_user_info(db, user)
    
    return removed_user

#-----------------------------------------------------------------#
