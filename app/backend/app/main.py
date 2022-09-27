# from pydantic import BaseModel, Field
# from uuid import uuid4
# from typing_extensions import Annotated
import schemas, models, services
from database import engine, SessionLocal
from fastapi import Depends, FastAPI, HTTPException
from datetime import datetime
from sqlalchemy.orm import Session

# BaseSQL.metadata.create_all(bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI(
    title="My title",
    description="My description",
    version="0.0.1",
)

@app.get("/")
def read_root():
    return "Hello et bienvenue sur ce simulateur de build Elden Ring"


@app.get("/date")
def get_date():
    current_date = datetime.today().strftime("%d %B %Y")
    return f"On est actuellement le {current_date}"


# @app.post("/activities/")
# def create_activity(activity : NewActivity):
#     return {"message":f"this activity has been successfully imported {activity}"}

@app.on_event("startup")
async def startup_event():
    models.BaseSQL.metadata.create_all(bind=engine)


# @app.get("/base_test")
# async def base_get():
#     BaseSQL.metadata.create_all(bind=engine)


@app.get("/db_connect")
async def get_connect():
    with engine.connect() as con:
        rs = con.execute('SELECT * FROM activities')
        for i in rs:
            print(i)
    # return i


@app.post("/users")
async def post_activities(activity: schemas.User, db: Session = Depends(SessionLocal)):
    db_user = services.get_user_by_id(activity.id, db)
    if db_user:
        raise HTTPException(status_code=400, detail="This activity already exist")
    services.create_user(db, activity)

