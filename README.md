# Fyyur Musicians Application

 Fyyur is a platform allowing musicians and venue owners to connect with each other. As an artists, you can establish a new profile with information about yourself and post
an image link. In addition, you may indicate whether you are currently seeking venues, and you can include a compelling message for venue owners who visit your profile. On the 
other side, venue are defined with the same information as artists, with the exception of a few fields. Although they are linked by a relationship named show, this form of relationship
can be categorized as many-to-many because an artist might have multiple shows at multiple venues and vice versa. Furthermore, the starting time of a show is recorded to
indicate when the show will begin, which could be in the past or the future.
 
 ## URL for the API (Base URL)
  Our API is hosted locally on the following address:
 ```bash
http://localhost:5000
 ```
  ## Getting Started
  To get started, make a new directory `fyyur` for the project files, `cd` to the project directory and make a [`virtual environment`](https://docs.python.org/3/library/venv.html), you should install the dependencies of this application, prepare the local development, and follow the hosting instructions.
  
  ### Dependencies
  
 - Python-3.8 and above.
 - VS code editor (or any code editer).
 - git.
 - PostgreSQL server.
 - Migration (for version control over the DB Schema).
 
 ### Python 
 
 And for the python packages, you can get them from the `requirements.txt` file in the project directory. You can install them all using the following command:
 
 ```
  pip3 install -r requirements.txt
 ```
  
  You can see your python packages using the following commands:
  ```
  pip3 freeze
  ```
  
  after you finish, you can run the app locally (in the project directory) using:
  ```
  python3 app.py
  ```
 - BUT you will have to setup Auth0 account to start using the application or testing it.
 
 ### PostgreSQL Server
 
 You shoule start by downloading the PostgreSQL Server on your machine. Go to this [`LINK`](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads) and download the installer.
 and after you finish installing the server, go the CLI (Command Line Interface) for the PostgreSQL server and do the following:
 
 - ### Windows
 
 Search for a program called `SQL Shell (psql)`, then you will see that it is asking you for the following information:
 
 - Server (Host address) for us it's local so just write this `localhost`.
 - Database (the database name) we will initialize one but for now just write `postgres` which is the default one.
 - Port `5432` is the default post for PostgreSQL server.
 - Username `postgres` it is the default user.
 - Password `postgres` is also the default passowrd.
 
 ### Note: make sure to change the database configuration on `config.py` file, otherwise nothing with the Migration will work.
 
 
 After you did the previous steps, you will see the following line (waiting for your commands):
 ```
 `postgres=# ` (postgres here is representating the DB name.
 ```
 
 Write the following to create a new database for the application called `fyyur`:
 ```
 CREATE DATABASE fyyur;
 ```
 
 You will get the following as a response (if the previous command is executed successfully)
 ```
 CREATE DATABASE
 ```
 
 from this step forward, the migration tool is going to take the rest of the work to be done.
 
 ### Migration
 
 This tool is controlling the Database Shcema in a way that we will never be worry about mistakes we did, because we can simply undo (using downgrade) the things we did to the schema,
and then we should commit (by upgrade command) every change we made to the schema.

Here, the library is installed from the previous step, and it's called `Flask_Migrate`. Now let's just run the CMD on windows, then `cd` to the project directory.
See the following command as an example:
```
cd C:\Users\PC01\Desktop\FCIT\Desktop\projects\Group Project\Fyyur_app
```
 
 After change the directory to the project directory, run the following command for initalizing the migration file (but this step is already done before),
and there's a command you should run before that, see the following
```
set FLASK_APP=app.py
set FLASK_DEBUG=true
```

These two previous commands will make the Migration tool see the app main file, and `FLASK_DEBUG` so when you 
run the application it will reload automatically with any changes on the file.

Now you can run the init command (But I previously mentioned that it's already done):
```
flask db init
```

Now, to really create the schema of the application (upgrade) command should be run to let the migration tool build the schema for you,
and it's also used to commit any changes on the database schema also, see the following:
```
flask db upgrade
```

And to undo any changes made on the schema, write the following command
```
flask db downgrade
```


## Running the Application Instructions (locally)

Open the CMD, `cd` to the project directory, then write the following:
```
set FLASK_APP=app.py
set FLASK_DEBUG=true
flask run
```

And if everything is running successfully, you will get the address for the website like this:
```
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 906-567-679
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Now, open your browser on the link provided from the CMD previously [`http://127.0.0.1:5000/`](http://127.0.0.1:5000/), and now tha application is running.

