# from pydantic import BaseModel, Field
# from uuid import uuid4
# from typing_extensions import Annotated
import schemas, models, services
from database import engine, SessionLocal
from fastapi import Depends, FastAPI, HTTPException
from datetime import datetime
from typing import Optional, List
from fastapi.middleware.cors import CORSMiddleware


models.BaseSQL.metadata.create_all(bind=engine)


app = FastAPI(
    title="My title",
    description="My description",
    version="0.0.1",
)

# origins = [
#     "http://localhost.tiangolo.com",
#     "https://localhost.tiangolo.com",
#     "http://localhost",
#     "http://localhost:8080",
# ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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

@app.get("/stats", status_code=200)
async def get_stats():
    all_stats = services.get_stats(db)
    return all_stats

@app.get("/users_summary", status_code=200)
async def display_all_users():
    all_names = services.get_summary(db) 
    return all_names

@app.get("/check_mdp", status_code=200)
async def check_infos(username, password):
    response = services.check_information(db, username, password)
    return response

@app.get("/compute_stats", status_code=200)
async def compute_stats(infos_json):
    response = services.compute_statistics(db, infos_json)
    return response

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

@app.post("/stat", status_code=200)
async def post_stat(stat: schemas.Stat):
    services.create_stat(db, stat)

@app.post("/test", status_code=200)
async def one_each():
    user1 = schemas.User(username="to_grt",
                        First_name="to_grt",
                        Last_name="to_grt",
                        age = 22,
                        email="to_grt",
                        password="to_grt")
    user2 = schemas.User(username="to_grt2",
                        First_name="to_grt2",
                        Last_name="to_grt2",
                        age = 23,
                        email="to_grt2",
                        password="to_grt2")    
    user3 = schemas.User(username="to_grt3",
                        First_name="to_grt3",
                        Last_name="to_grt3",
                        age = 24,
                        email="to_grt3",
                        password="to_grt3")                                         
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
    stat1 = schemas.Stat(dexterity=0,
                        faith=666,
                        arcane=324,
                        mind=7,
                        strength=5,
                        intelligence=999,
                        vigor=12,
                        endurance=546)
    stat2 = schemas.Stat(dexterity=1,
                        faith=2,
                        arcane=3,
                        mind=4,
                        strength=5,
                        intelligence=6,
                        vigor=7,
                        endurance=8)
    stat3 = schemas.Stat(dexterity=9,
                        faith=10,
                        arcane=11,
                        mind=12,
                        strength=13,
                        intelligence=14,
                        vigor=15,
                        endurance=16)
    services.create_item(db, item1)
    services.create_item(db, item2)
    services.create_item(db, item3)
    services.create_user(db, user1)
    services.create_user(db, user2)
    services.create_user(db, user3)
    services.create_user_build(db, user_build1)
    services.create_user_build(db, user_build2)
    services.create_user_build(db, user_build3)
    services.create_stat(db, stat1)
    services.create_stat(db, stat2)
    services.create_stat(db, stat3)

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

@app.delete("/delete_stat")
async def delete_stat(id:int):
    removed_stat = services.delete_stat(db, id)
    return removed_stat

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
