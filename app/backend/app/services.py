from sqlalchemy.orm import Session
from fastapi import HTTPException
import schemas, models


# get activity by ID to be sure we don't post the same
def get_user_by_id(post_id: str, db: Session) -> models.User:
    record = db.query(models.User).filter(models.User.id == post_id).first()
    if not record:
        raise HTTPException(status_code=404, detail="Not Found")
    record.id = str(record.id)
    return record


# create the activity in call in the 'main.py' to post the activity
def create_user(db: Session, post: schemas.User) -> models.User:
    record = db.query(models.User).filter(models.User.id == post.id).first()
    if record:
        raise HTTPException(status_code=409, detail="Already exists")
    db_post = models.User(**post.dict())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    db_post.id = str(db_post.id)
    return db_post
