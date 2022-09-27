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
    current_date = datetime.today().strftime("%d %B %Y")
    return f"On est actuellement le {current_date}"


# @app.on_event("startup")
# async def startup_event():
#     models.BaseSQL.metadata.create_all(bind=engine)


# @app.get("/base_test")
# async def base_get():
#     BaseSQL.metadata.create_all(bind=engine)




@app.get("/users", status_code = 200)
def get_all_users():
    users_all = db.query(models.User).all()
    
    return users_all


#do basically the same as above function
# @app.get("/db_connect")
# async def get_connect():
#     with engine.connect() as con:
#         rs = con.execute('SELECT * FROM users;')
#         for i in rs:
#             print(i)
#     return i


@app.post("/users")
async def post_activities(activity: schemas.User):
    # db_user = services.get_user_by_id(activity.id, db)
    services.create_user(db, activity)

