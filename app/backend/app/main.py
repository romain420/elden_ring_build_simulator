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
@app.get("/users", status_code = 200)
def get_all_users():
    all_users = services.get_user(db)
    
    return all_users

@app.post("/users")
async def post_user(user: schemas.User):
    services.create_user(db, user)
   
#this API as to be avoid 
# @app.delete("/delete_user")
# async def remove_user(user:schemas.User):
#     deleted_user = services.delete_user_by_name(db, user)
    
#     return deleted_user

@app.put("/user_last_visit")#TODO don't forget to change the name by 'update_user_info'
async def update_last_visit(user:schemas.User):
    update_user = services.update_user_info(db, user)
    
    return update_user

@app.put("/delete_user")
async def delete_user(user:schemas.User):
    removed_user = services.kill_user_info(db, user)
    
    return removed_user
#-----------------------------------------------------------------#
