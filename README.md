# Elden Ring Build Simulator

Welcome in our Elden Ring build simulator. For the moment, it's only a pre-release where you can only compute your character's statistics without any stuff. But stay tune! In a few weeks, new features will be added! 

## Getting started

For the moment, our simulator is not released online. But you can make the app **run** with only a few command ! 
This is the objectif of this document. We will explain how to **launch our app** on your own system.  

### Prerequisites  

There is not a lot of prerequisites. But it is necessary to respect them.  

You need to have:  
- Git 
- Docker  

Installed on your distribution.  

Normally you can launch app without any issues on the distribution of your choice: Linux *(Debian base)*, Windows and MAC *(but we didn't have the opportunity to test for the last one)*.  

If you respect those conditions, we can go for the next step!  

### Installation  

In this part we will see how to get the project on your system.  

1. Open **Terminal** or a **PowerShell** (if you are on Windows)
2. Then enter the following command:  
```bash
git clone <repository_link>
```  
Normally you should be able to see the **elden_ring_build_simulator** folder if you write the command `ls`.  

### App launching

Now let's start the tricky part. We are going to **launch the app** with only a few command.   

1. Make sure you are in the project folder with the command  
```bash
cd ./elden_ring_build_simulator
``` 
2. Now enter in the **app** folder with this command  
```bash
cd ./app
```
You should see the following path in your command line `~/elden_ring_build_simulator/app$`  
3.Now is the most important step! Be carefull it will go fast ! Enter this command  
```bash
docker-compose up -d
```  
*You can remove the `-d` argument if you want to have logs from all different containers insides the app*  
4. Let it load and you will see
```bash
Creating network "app_default" with the default driver
Creating app_db_1  ... done
Creating app_app_1 ... done
Creating app_api_1 ... done
```
You can run the following command  
```bash
docker ps
``` 
and you should see something like this  
```bash
CONTAINER ID   IMAGE      COMMAND                  CREATED          STATUS          PORTS                                               NAMES
************   app_api    "uvicorn main:app --…"   52 minutes ago   Up 52 minutes   80/tcp, 0.0.0.0:5000->5000/tcp, :::5000->5000/tcp   app_api_1
************   app_app    "docker-entrypoint.s…"   52 minutes ago   Up 52 minutes   0.0.0.0:8000->3000/tcp, :::8000->3000/tcp           app_app_1
************   postgres   "docker-entrypoint.s…"   52 minutes ago   Up 52 minutes   0.0.0.0:5432->5432/tcp, :::5432->5432/tcp           app_db_1
```
If it is the case, great news! It is running perfectly!  

## The App 

As you can see with the last command, *App* is composed of 3 differents containers. 

### Backend
Backend is composed of 2 different parts.

#### API 

```bash
CONTAINER ID   IMAGE      COMMAND                  CREATED          STATUS          PORTS                                               NAMES
************   app_api    "uvicorn main:app --…"   52 minutes ago   Up 52 minutes   80/tcp, 0.0.0.0:5000->5000/tcp, :::5000->5000/tcp   app_api_1
```
This container is the one that makes the interface between our **frontend app** and the **database**. It is host on port 5000, to access it, just enter `localhost:5000` or `127.0.0.1:5000` in your browser navigator
It is a classical **REST API** realised with the [FastAPI](https://fastapi.tiangolo.com/) framework, where you can execute `GET`, `POST`, `PUT` and `DELETE` requests.  
*If you want to access all of the API methods you can enter `localhost:5000/docs`*

#### Database  
```bash
CONTAINER ID   IMAGE      COMMAND                  CREATED          STATUS          PORTS                                               NAMES
************   postgres   "docker-entrypoint.s…"   52 minutes ago   Up 52 minutes   0.0.0.0:5432->5432/tcp, :::5432->5432/tcp           app_db_1
```
This is our database. It is a [Postgres](https://www.postgresql.org/) database and it is composed of 5 different tables. 

To check the table content, you have to enter inside the container with the following command: 
```bash
docker exec -it <container_id> bash
```
Now you should be inside container. To enter the database itself you can run this command: 
```bash
psql <database_name> <user_name>
```
*database name and user name are inside `app/backend/.env`*

Finally you can run the SQL command to check the table content *(at the begining they should be empty)*.
```bash
SELECT * FROM users;
```
*don't forget `;` at the end of request*

### Frontend 

Finally the last part of the application: **the frontend**.  

```bash
CONTAINER ID   IMAGE      COMMAND                  CREATED          STATUS          PORTS                                               NAMES
************   app_app    "docker-entrypoint.s…"   52 minutes ago   Up 52 minutes   0.0.0.0:8000->3000/tcp, :::8000->3000/tcp           app_app_1
```

This is a frontend created with the framework [React](https://fr.reactjs.org/) that links 2 differents **API**: one is an open source [elden ring](https://eldenring.fanapis.com/) to get all items, weapon, stuff from the game. And the second one is our **API** that store user's information.

## Finally

I hope this little tutorial have been clear enough, enjoy the app!  
If you face any issue or have any idea to improve the app leave a comment on [Issues](https://gitlab.com/RomainD_/elden_ring_build_simulator/-/issues). 

And do not hesitate to check [Wiki](https://gitlab.com/RomainD_/elden_ring_build_simulator/-/wikis/home) for more details. 




