# from msilib import schema
from typing import List
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import select
from fastapi import HTTPException
import schemas, models
from datetime import datetime


#--------------------------user methods--------------------------#

#---------------------GET PART---------------------#
def get_users(db: Session):
    all_users = db.query(models.User).all()
    return all_users

def get_all_user_builds(db: Session):
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

def get_user_builds(db:Session, username:str):
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user:
        return "This user does not exist"
    if user.nb_builds == 0:
        return "This user does not have any build"
    to_return = "Here are the builds of the user: " + user.username + "     implement here loop for builds" #TODO
    return to_return

#---------------------CREATION PART---------------------#
def create_user(db: Session, post: schemas.User) -> models.User:#TODO add condition to check if email adress or username is already use
    record = db.execute(select(models.User).where(models.User.username == post.username)).first()
    if record:
        raise HTTPException(status_code=409, detail= f"This username already exists, please choose another one")
    user = models.User(**post.dict())
    db.add(user)
    db.commit()
    return user

def create_user_build(db: Session, post: schemas.User_build) -> models.User_build:
    user_build = models.User_build(**post.dict())
    owner_username = user_build.owner_username
    user = db.query(models.User).filter(models.User.username == owner_username).first()
    if not user:
        return "This user does not exist"
    user.nb_builds += 1
    db.add(user_build)
    db.commit()
    return user_build

def create_item(db: Session, post: schemas.Item) -> models.Item:
    record = db.execute(select(models.Item).where(models.Item.name == post.name)).first()
    if record:
        raise HTTPException(status_code=409, detail= f"This Item already exists")
    item = models.Item(**post.dict())
    db.add(item)
    db.commit()
    return item

#---------------------UPDATE PART---------------------#
#update fields in table User
def update_user_info(db:Session, update:schemas.User):#TODO try to update 1 field for the moment after that let's update 1 or more field at the same time
    record = db.query(models.User).filter(models.User.id == update.id).first()
    if not record:
        raise HTTPException(status_code=404, detail= f"User {update.First_name} {update.Last_name} doesn't exist. We can't modify it.")
    
    record.last_visit = datetime.today()
    db.commit()
    
    return f"{update.First_name} {update.Last_name} as log in {update.last_visit}"
#models.User.last_visit == update.last_visit

#---------------------DELETE PART---------------------#
#this methode is suppose to remove all user info exept 'id' if user decide to remove his account
def kill_user_info(db:Session, username:str):#TODO find a more complient way to smash the data (for loop or something)
    record = db.query(models.User).filter(models.User.username == username).first()
    if not record:
        raise HTTPException(status_code=404, detail= f"User {username} doesn't exist. We can't delete it.")
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

def delete_user(db:Session, username:str):
    record = db.query(models.User).filter(models.User.username == username).first()
    if not record:
        raise HTTPException(status_code=404, detail= f"User {username} doesn't exist. We can't delete it.")
    db.delete(record)
    db.commit()
    
def delete_item(db:Session, name:str):
    record = db.query(models.Item).filter(models.Item.name == name).first()
    if not record:
        raise HTTPException(status_code=404, detail= f"Item {name} doesn't exist. We can't delete it.")
    db.delete(record)
    db.commit()

def delete_user_build(db:Session, id:int):
    record = db.query(models.User_build).filter(models.User_build.id == id).first()
    if not record:
        raise HTTPException(status_code=404, detail= f"User_build {id} doesn't exist. We can't delete it.")
    db.delete(record)
    db.commit()

    
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