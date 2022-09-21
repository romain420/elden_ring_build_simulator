from sqlalchemy.orm import Session
from fastapi import HTTPException
# from . import schemas, models
from schemas import User as Schemas_User
from models import User as Models_User


# get activity by ID to be sure we don't post the same
def get_user_by_id(post_id: str, db: Session) -> Models_User:
    record = db.query(Models_User).filter(Models_User.id == post_id).first()
    if not record:
        raise HTTPException(status_code=404, detail="Not Found")
    record.id = str(record.id)
    return record


# create the activity in call in the 'main.py' to post the activity
def create_user(db: Session, post: Schemas_User) -> Models_User:
    record = db.query(Models_User).filter(Models_User.id == post.id).first()
    if record:
        raise HTTPException(status_code=409, detail="Already exists")
    db_post = Models_User(**post.dict())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    db_post.id = str(db_post.id)
    return db_post
