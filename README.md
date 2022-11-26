# Elden Ring Build Simulator

Welcome inside our Elden Ring build simulator. For the moment it's only a pre-release where you can only calcule your character statistics without any stuff. But stay tune in some few weeks new features will be add ! 

## Getting started

For the moment our simulator is not release online. But you can make the app **run** with only few command ! 
This is the objectif of this part. We will explain you how to **launch our app** on your own system.  

### Prerequisites  

There is not a lot of prerequisites. But it is necessary to respect them.  

You need to have :  
- Git 
- Docker  

Install on your distribution.  

Normally you can launch app without any issues on destribution of your choice Linux *(Debian base)*, Windows and MAC *(but we don't had opportunity to test for the last one)*.  

If you respect those conditions we can go for the next step !  

### Installation  

In this part we will see how to get the project on your system.  

1. Open **Terminal** or a **PowerShell** (if you are on Windows)
2. Then unter the following command :  
```bash
git clone <repository_link>
```  
Normally you should be able to see **elden_ring_build_simulator** folder if you write command `ls`.  

### App launching

Now let's past in a little bit more tricky part. We are going to **launch the app** with only few command.  

1. Make sure you are in project folder with command  
```bash
cd ./elden_ring_build_simulator
``` 
2. Now enter in folder **app** with this command  
```bash
cd ./app
```
You should see the following path in your command line `~/elden_ring_build_simulator/app$`  
3.Now is the most important step ! Be carefull it's going to be fast ! Unter this command  
```bash
docker-compose up -d
```  
*You can remove the `-d` argument if you want to have logs from all differents containers insides the app*  
4. Let it load a little bit and after see  
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
If it's the case, I have a great new the is running perfectly !  

## The App 

As you can see in last command *App* is composed of 3 differents containers. 

### Backend
Backent is composed of 2 differnet part.

#### API 

```bash
CONTAINER ID   IMAGE      COMMAND                  CREATED          STATUS          PORTS                                               NAMES
************   app_api    "uvicorn main:app --…"   52 minutes ago   Up 52 minutes   80/tcp, 0.0.0.0:5000->5000/tcp, :::5000->5000/tcp   app_api_1
```
This container the one that make the interface between our **frontend app** and the **database**. It is host on port 5000, to access it just unter `localhost:5000` or `127.0.0.1:5000` in your browser nav
It is a classical **REST API** realise with [FastAPI](https://fastapi.tiangolo.com/) framework, where you can execute `GET`, `POST`, `PUT` and `DELETE` request.  
*If you want access all API methods you can unter `localhost:5000/docs`*

#### Database  
```bash
CONTAINER ID   IMAGE      COMMAND                  CREATED          STATUS          PORTS                                               NAMES
************   postgres   "docker-entrypoint.s…"   52 minutes ago   Up 52 minutes   0.0.0.0:5432->5432/tcp, :::5432->5432/tcp           app_db_1
```
This is our database. It is a [Postgres](https://www.postgresql.org/) databas and it's compose of 5 differents table. 

To check the table content you have to unter the container with the following command : 
```bash
docker exec -it <container_id> bash
```
Now you should be inside container. To enter the database itself you can run this command : 
```bash
psql <database_name> <user_name>
```
*database name and user name are inside `app/backend/.env`*

Finally you can run SQL command to check the table content *(at the begining they shoudl be empty)*.
```bash
SELECT * FROM users;
```
*don't forget `;` at the end of request*

### Frontend 

Finally the last part of the application **the frontend**.  

```bash
CONTAINER ID   IMAGE      COMMAND                  CREATED          STATUS          PORTS                                               NAMES
************   app_app    "docker-entrypoint.s…"   52 minutes ago   Up 52 minutes   0.0.0.0:8000->3000/tcp, :::8000->3000/tcp           app_app_1
```

This is a frontend realise with framework [React](https://fr.reactjs.org/) that is link to 2 differents **API** one is an open source [elden ring](https://eldenring.fanapis.com/) to get all items, weapon, stuff from the game. And the second one is our **API** that store user information.

## Finally

I hope this little tutorial have been clear enough, enjoi the app !  
If you face any issue or have some idea to upgrade the app leave a comment on [Issues](https://gitlab.com/RomainD_/elden_ring_build_simulator/-/issues). 

And don't hesitate to check [Wiki](https://gitlab.com/RomainD_/elden_ring_build_simulator/-/wikis/home) for more details. 




