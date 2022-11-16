# from pydantic import BaseModel, Field
# from uuid import uuid4
# from typing_extensions import Annotated
import schemas, models, services
from database import engine, SessionLocal
from fastapi import Depends, FastAPI, HTTPException
from datetime import datetime
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
async def get_all_users():
    all_users = services.get_users(db)
    return all_users

@app.get("/user_builds", status_code=200)
async def get_all_user_builds():
    all_user_builds = services.get_all_user_builds(db)
    return all_user_builds

@app.get("/items", status_code=200)
async def get_items():
    all_items = services.get_items(db)
    return all_items

@app.get("/users_summary", status_code=200)
async def display_all_users():
    all_names = services.get_summary(db) 
    return all_names

@app.get("/{username}", status_code=200)
async def display_specific_user(username):
    user_infos = services.get_user_infos(db, username)
    return user_infos

@app.get("/{username}/builds", status_code=200)
async def display_user_builds(username):
    user_builds = services.get_user_builds(db, username)
    return user_builds

#-------------POST PART-------------#
@app.post("/user", status_code=200)
async def post_user(user: schemas.User):
    services.create_user(db, user)

@app.post("/user_build", status_code=200)
async def post_user_build(user_build: schemas.User_build):
    services.create_user_build(db, user_build)

@app.post("/item", status_code=200)
async def post_item(item: schemas.Item):
    services.create_item(db, item)

@app.post("/test", status_code=200)
async def one_each():
    user1 = schemas.User(username="to_grt",
                        First_name="to_grt",
                        Last_name="to_grt",
                        date_of_birth="2022-11-11T22:17:05.260Z",
                        email="to_grt",
                        password="to_grt",
                        created_at="2022-11-11T22:17:05.260Z",
                        last_visit="2022-11-11T22:17:05.260Z",
                        nb_builds=0,
                        builds=[])
    user2 = schemas.User(username="to_grt2",
                        First_name="to_grt2",
                        Last_name="to_grt2",
                        date_of_birth="2022-11-11T22:17:05.260Z",
                        email="to_grt2",
                        password="to_grt2",
                        created_at="2022-11-11T22:17:05.260Z",
                        last_visit="2022-11-11T22:17:05.260Z",
                        nb_builds=0,
                        builds=[])    
    user3 = schemas.User(username="to_grt3",
                        First_name="to_grt3",
                        Last_name="to_grt3",
                        date_of_birth="2022-11-11T22:17:05.260Z",
                        email="to_grt3",
                        password="to_grt3",
                        created_at="2022-11-11T22:17:05.260Z",
                        last_visit="2022-11-11T22:17:05.260Z",
                        nb_builds=0,
                        builds=[])                                         
    item1 = schemas.Item(name="item1",
                        image="item1",
                        description="item1",
                        category="item1",
                        dmg_negation=[],
                        resistance=[],
                        weight=10)
    item2 = schemas.Item(name="item2",
                        image="item2",
                        description="item2",
                        category="item2",
                        dmg_negation=[],
                        resistance=[],
                        weight=10)
    item3 = schemas.Item(name="item3",
                        image="item3",
                        description="item3",
                        category="item3",
                        dmg_negation=[],
                        resistance=[],
                        weight=10)                                                
    user_build1 = schemas.User_build(name="build1",
                                    image="b",
                                    created_at="2022-11-11T22:17:05.260Z",
                                    last_visit="2022-11-11T22:17:05.260Z",
                                    last_update="2022-11-11T22:17:05.260Z",
                                    nb_visits=0,
                                    nb_items=0,
                                    items_id=[],
                                    owner_username="to_grt")
    user_build2 = schemas.User_build(name="build2",
                                    image="b",
                                    created_at="2022-11-11T22:17:05.260Z",
                                    last_visit="2022-11-11T22:17:05.260Z",
                                    last_update="2022-11-11T22:17:05.260Z",
                                    nb_visits=0,
                                    nb_items=0,
                                    items_id=[],
                                    owner_username="to_grt")
    user_build3 = schemas.User_build(name="build3",
                                    image="b",
                                    created_at="2022-11-11T22:17:05.260Z",
                                    last_visit="2022-11-11T22:17:05.260Z",
                                    last_update="2022-11-11T22:17:05.260Z",
                                    nb_visits=0,
                                    nb_items=0,
                                    items_id=[],
                                    owner_username="to_grt")
    services.create_item(db, item1)
    services.create_item(db, item2)
    services.create_item(db, item3)
    services.create_user(db, user1)
    services.create_user(db, user2)
    services.create_user(db, user3)
    services.create_user_build(db, user_build1)
    services.create_user_build(db, user_build2)
    services.create_user_build(db, user_build3)

@app.post("/delete_user_post")
async def delete_user(username:str):
    removed_user = services.delete_user(db, username)
    return removed_user

#-------------PUT PART-------------#
@app.put("/user_last_visit")#TODO don't forget to change the name by 'update_user_info'
async def update_last_visit(user:schemas.User):
    update_user = services.update_user_info(db, user)
    return update_user

@app.put("/kill_user")
async def delete_user(username:str):
    removed_user = services.kill_user_info(db, username)
    return removed_user

#-------------DELETE PART-------------#
@app.delete("/force_delete_user")           # Don't ever use this, except for debugging or testing purposes
async def delete_user(username:str):
    removed_user = services.force_delete_user(db, username)
    return removed_user

@app.delete("/delete_user")
async def delete_user(username:str):
    removed_user = services.delete_user(db, username)
    return removed_user

@app.delete("/delete_item")
async def delete_item(name:str):
    removed_item = services.delete_item(db, name)
    return removed_item

@app.delete("/delete_user_build")
async def delete_user(id:int):
    removed_user_build = services.delete_user_build(db, id)
    return removed_user_build

@app.delete("/delete_user_build_from_username")
async def delete_user_build_from_username(username:str, build_name:str):
    removed_user_build = services.delete_user_build_from_username(db, username, build_name)
    return removed_user_build

@app.delete("/clear_tables")
async def clear_tables():
    removed = services.clear_data(db)
    return removed
#-----------------------------------------------------------------#
