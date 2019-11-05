# Airbnb clone app

## Cloning Airbnb using Python, Django, tailwind and more.. ✈️🏠

### create virtual environment

mkdir "project folder"  
cd "project folder"  
pipenv --three (install python 3)  
code . (we can see pipfile which is like package.json)  
pipenv shell (go inside the virtual environment)  
pipenv install Django==2.2.5 (install django)  
Django-admin (we could check if its installed)  

django-admin startproject config (create django config files)  
put config folder and manage.py outside  


> python is runtime language, not compiler.  
 so, it cannot check errors before programs start.  
the solution is linter!


sudo lsof -t -i tcp:8000 | xargs kill -9  
python manage.py migrate  
python manage.py makemigrations  

> makemigrations checks for changes on the data shape and creates a file describing the changes.
migrate applies the migrations to the database!
The tables and everything are created automatically by Django with 'migrate'


python manage.py runserver  
python manage.py createsuperuser  

* divide and conquer django applications!!

### Django
[django documentation](https://docs.djangoproject.com/en/2.2/)

> framework is that we have to follow their rules like specific words or file names, but library is that we use to build  

1. django-admin startapp "application name" (이름은 복수여야함!)  
2. make models of each applications
3. add config to settings.py (PROJECT_APPS = ["users.apps.UsersConfig", "rooms.apps.RoomsConfig"])

...


```
if we see this error, then delete db.sqlite3 file and run makemigrations, migrate.
django.db.migrations.exceptions.InconsistentMigrationHistory: Migration admin.0001_initial is applied before its dependency users.0001_initial on database 'default'.
```

* django connect to db with **ORM(object relational mapping)** which changes python code to SQL so that db could understand it.