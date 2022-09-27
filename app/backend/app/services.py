from sqlalchemy.orm import Session
from fastapi import HTTPException
import schemas, models

#--------------------------user methods--------------------------#
# get activity by ID to be sure we don't post the same
# def get_user_by_id(post_id: str, db: Session) -> models.User:
#     record = db.query(models.User).filter(models.User.id == post_id).first()
#     if not record:
#         # raise HTTPException(status_code=404, detail="Not Found")
#         message = "This user doesn't exist. It's going to be created !"
#     else:
#         record.id = str(record.id)
#         message = record
#     return message

#get all the line from table User
def get_user(db: Session):
    users_all = db.query(models.User).all()
    return users_all


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

#delete ligne in table User
def delete_user_by_name(db: Session, delete:schemas.User):
    record = db.query(models.User).filter(models.User.First_name == delete.First_name).first()
    if not record:
        raise HTTPException(status_code=404, detail= "This user doesn't exist. We can't delete it...")
    db.delete(record)
    db.commit()
    return "The user : {delete.First_name} has been deleted successfully"
#-----------------------------------------------------------------#