# from msilib import schema
from typing import List
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import select
from fastapi import HTTPException
import schemas, models, calculus_ligth
from datetime import datetime
import json


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

def get_stats(db: Session):
    all_stats = db.query(models.Stat).all()
    return all_stats

def get_charac_stats(db: Session):
    all_stats = db.query(models.CharacStats).all()
    return all_stats

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
    update_last_visit(db, user.username)
    to_return = {
        "username":user.username,
        "First_name": user.First_name,
        "Last_name": user.Last_name,
        "nb_builds":str(user.nb_builds),
        "last_visit":str(user.last_visit),
        "builds": ', '.join(user.builds)
    }
    return user

def get_user_builds(db:Session, username:str):
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user:
        return "This user does not exist"
    if user.nb_builds == 0:
        return "This user does not have any build"
    to_return = "Here are the builds of the user: " + user.username + ":"
    for build in user.builds:
        user_build = db.query(models.User_build).filter(models.User_build.name == build, models.User_build.owner_username == username).first()
        to_return += "    " + build + " contains: " + user_build.items_id
    return to_return

def check_information(db:Session, username:str, password:str):
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user:
        return "This user does not exist"
    if user.password != password:
        return "Wrong password, please check your informations"
    to_return = get_user_infos(db, username)
    return to_return

def compute_statistics(db:Session, infos_json:str):
    infos_dict = json.loads(infos_json)   # string json to python dictionary
    stats = models.Stat(**infos_dict)
    response_stat = calculus_ligth.stats(int(stats.vigor), int(stats.mind), int(stats.endurance), int(stats.strength), int(stats.dexterity), int(stats.intelligence), int(stats.faith), int(stats.arcane))
    create_charac_stats_with_dict(db, response_stat)
    return response_stat

#---------------------CREATION PART---------------------#
def create_user(db: Session, post: schemas.User) -> models.User:
    check_username = db.execute(select(models.User).where(models.User.username == post.username)).first()
    if check_username:
        raise HTTPException(status_code=409, detail= f"This username already exists, please choose another one")
    check_email = db.execute(select(models.User).where(models.User.email == post.email)).first()
    if check_email:
        raise HTTPException(status_code=409, detail= f"This email already exists, please choose another one")
    mandatory_dict = {'created_at': datetime.today(), 'last_visit': datetime.today(), 'nb_builds': 0, 'builds': []}
    final_dict = {**post.dict(), **mandatory_dict}
    user = models.User(**final_dict)
    db.add(user)
    db.commit()
    return user

def create_user_build(db: Session, post: schemas.User_build) -> models.User_build:
    user_build = models.User_build(**post.dict())
    owner_username = user_build.owner_username
    user = db.query(models.User).filter(models.User.username == owner_username).first()
    if not user:
        raise HTTPException(status_code=404, detail= f"This user does not exist, cannot create a build for it")
    db.query(models.User).filter(models.User.username == owner_username).update({"builds": models.User.builds + [user_build.name]})
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

def create_stat(db:Session, post: schemas.Stat) -> models.Stat:
    stats = models.Stat(**post.dict())
    db.add(stats)
    db.commit()
    return stats

def create_charac_stats(db:Session, post: schemas.CharacStats) -> models.CharacStats:
    charac_stats = models.CharacStats(**post.dict())
    db.add(charac_stats)
    db.commit()
    return charac_stats

def create_charac_stats_with_dict(db:Session, dictionary: models.CharacStats) -> models.CharacStats:
    charac_stats = models.CharacStats(**dictionary)
    db.add(charac_stats)
    db.commit()
    return charac_stats

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

def update_last_visit(db:Session, username:str):
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail= f"This user doesn't exist. We can't update it.")
    user.last_visit = datetime.today()
    db.commit()

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

def force_delete_user(db:Session, username:str):    #Don't ever use that, except for debugging or test purposes
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail= f"User {username} doesn't exist. We can't delete it.")
    db.delete(user)
    db.commit()
    return "user has been force deleted with success, be careful and look out for orphan user_builds"

def delete_user(db:Session, username:str):
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail= f"User {username} doesn't exist. We can't delete it.")
    db.query(models.User_build).filter(models.User_build.owner_username == username).delete()
    db.delete(user)
    db.commit()
    return "user deleted with success"
    
def delete_item(db:Session, name:str):
    record = db.query(models.Item).filter(models.Item.name == name).first()
    if not record:
        raise HTTPException(status_code=404, detail= f"Item {name} doesn't exist. We can't delete it.")
    db.delete(record)
    db.commit()
    return "item deleted with success, this should not happen, be careful for user_builds with missing items"

def delete_stat(db:Session, id:int):
    stat = db.query(models.Stat).filter(models.Stat.id == id).first()
    if not stat:
        raise HTTPException(status_code=404, detail= f"Stat n°{id} doesn't exist. We can't delete it.")
    db.delete(stat)
    db.commit()
    return "stat deleted with success"

def delete_charac_stats(db:Session, id:int):
    charac_stat = db.query(models.CharacStats).filter(models.CharacStats.id == id).first()
    if not charac_stat:
        raise HTTPException(status_code=404, detail= f"Character Statistics n°{id} doesn't exist. We can't delete it.")
    db.delete(charac_stat)
    db.commit()
    return "Character Statistics deleted with success"

def delete_user_build(db:Session, id:int):
    build = db.query(models.User_build).filter(models.User_build.id == id).first()
    if not build:
        raise HTTPException(status_code=404, detail= f"User_build {id} doesn't exist. We can't delete it.")
    owner = db.query(models.User).filter(models.User.username == build.owner_username).first()
    if not owner:
        raise HTTPException(status_code=404, detail= f"User_build {id} doesn't have an owner, this shouldn't be possible. We can't delete it.")
    owner.nb_builds -= 1
    db.delete(build)
    db.commit()
    return "user_build deleted with success"

def delete_user_build_from_username(db:Session, username:str, build_name:str):
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail= f"This user:" + username + " doesn't exist.")
    user_build = db.query(models.User_build).filter(models.User_build.name == build_name, models.User_build.owner_username == user.username).first()
    if not user_build:
        raise HTTPException(status_code=404, detail= f"This build: " + build_name + " for the user:" + username + " doesn't exist. We can't delete it.")
    user.nb_builds -= 1
    user.builds.remove(user_build.name)
    db.delete(user_build)
    db.commit()
    return "user_build deleted with success"

def clear_data(db:Session): # /!\ Clear all the tables, be careful
    db.query(models.User_build).delete()
    db.query(models.Item).delete()
    db.query(models.User).delete()
    db.query(models.Stat).delete()
    db.query(models.CharacStats).delete()
    db.commit()
    return "all tables has been clear"