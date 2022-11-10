# from msilib import schema
from typing import List
from sqlalchemy.orm import Session
from fastapi import HTTPException
import schemas, models
from datetime import datetime


#--------------------------user methods--------------------------#
def get_users(db: Session):
    all_users = db.query(models.User).all()
    return all_users

def get_user_builds(db: Session):
    all_user_builds = db.query(models.User_build).all()
    return all_user_builds

def get_items(db: Session):
    all_items = db.query(models.Item).all()
    return all_items

def get_summary(db:Session):
    all_last_name = db.query(models.User.Last_name).all()
    all_first_name = db.query(models.User.First_name).all()
    all_last_visit = db.query(models.User.last_visit).all()
    result = ""
    for index in range(len(all_last_name)):
        if index != 0: result += "    |    "
        result += all_last_name[index][0] + " " + all_first_name[index][0] + " " + all_last_visit[index][0].strftime("%H:%M:%S")
    return result

def get_user_infos(db:Session, username:str):
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user:
        return "This user does not exist"
    to_return = "This user exists:    username: " + user.username + "    First name: " + user.First_name + "     Last name: " + user.Last_name
    return to_return

# create the activity in call in the 'main.py' to post the activity
def create_user(db: Session, post: schemas.User) -> models.User:#TODO add condition to check if email adress or username is already use
    record = db.query(models.User).filter(models.User.id == post.id).first()
    if record:
        raise HTTPException(status_code=409, detail= f"This user already exists")
    db_post = models.User(**post.dict())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    db_post.id = str(db_post.id)
    return db_post

def create_user_build(db: Session, post: schemas.User_build) -> models.User_build:
    record = db.query(models.User_build).filter(models.User_build.id == post.id).first()
    if record:
        raise HTTPException(status_code=409, detail= f"This user_build already exists")
    db_post = models.User_build(**post.dict())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    db_post.id = str(db_post.id)
    return db_post

def create_item(db: Session, post: schemas.Item) -> models.Item:
    record = db.query(models.Item).filter(models.Item.id == post.id).first()
    if record:
        raise HTTPException(status_code=409, detail= f"This item already exists")
    db_post = models.Item(**post.dict())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    db_post.id = str(db_post.id)
    return db_post

#update fields in table User
def update_user_info(db:Session, update:schemas.User):#TODO try to update 1 field for the moment after that let's update 1 or more field at the same time
    record = db.query(models.User).filter(models.User.id == update.id).first()
    if not record:
        raise HTTPException(status_code=404, detail= f"User {update.First_name} {update.Last_name} doesn't exist. We can't modify it.")
    
    record.last_visit = datetime.today()
    db.commit()
    
    return f"{update.First_name} {update.Last_name} as log in {update.last_visit}"
#models.User.last_visit == update.last_visit

#this methode is suppose to remove all user info exept 'id' if user decide to remove his account
def kill_user_info(db:Session, update:schemas.User):#TODO find a more complient way to smash the data (for loop or something)
    record = db.query(models.User).filter(models.User.id == update.id).first()
    if not record:
        raise HTTPException(status_code=404, detail= f"User {update.First_name} {update.Last_name} doesn't exist. We can't modify it.")
    # update_dict = dict(update)
    # # list_fields = update_dict
    # list_record = []
    # for i in list(update_dict.keys())[1:]:#TODO maybe add a contidition on field type 
    #     # print(i)
    #     # list_record.append(record.i) #= "none"
    record.First_name = "none"
    record.Last_name = "none"
    record.username = "none"
    record.date_of_birth = datetime(1, 1, 1, 0, 0)
    record.email = "none"
    record.password = "none"
    record.created_at = datetime(1, 1, 1, 0, 0)
    record.last_visit = datetime(1, 1, 1, 0, 0)
    record.nb_builds = -1
    record.builds = "none"
    db.commit()
    return "This user have been succesfully deleted"#f"this is the record list {list_record}"#
    
#********this methode is not alwode because we can not remove a masterdata from db********#
#delete ligne in table User
# def delete_user_by_name(db: Session, delete:schemas.User):
#     record = db.query(models.User).filter(models.User.First_name == delete.First_name).first()
#     if not record:
#         raise HTTPException(status_code=404, detail= f"User {delete.First_name} doesn't exist. We can't delete it.")
#     db.delete(record)
#     db.commit()
#     return f"The user : {delete.First_name} has been deleted successfully"
#******************************************************************************************#
#-----------------------------------------------------------------#