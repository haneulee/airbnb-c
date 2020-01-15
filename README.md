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
4. make fields and fieldset
5. [how to connect with django models](https://docs.djangoproject.com/en/2.2/ref/models/querysets/)
    - python manage.py shell
    - from users.models import User
    - dir(User) or vars(User)
    - all_user = User.objects.all()
    - all_user.filter(superhost=True)
    - from rooms.models import Room
    - Room.review_set.all()

...


```
if we see this error, then delete db.sqlite3 file and run makemigrations, migrate.
django.db.migrations.exceptions.InconsistentMigrationHistory: Migration admin.0001_initial is applied before its dependency users.0001_initial on database 'default'.
```

* django connect to db with **ORM(object relational mapping)** which changes python code to SQL so that db could understand it.

* **foreign key** provide a many-to-one relation.

### tailwind CSS

npm install gulp gulp-postcss gulp-sass gulp-csso node-sass -d
npm installl tailwindcss -d
npx tailwind init
npm install autoprefixer -d

### translation

1. make "locale" folder
2. brew install gettext
3. brew link gettext --force
4. {% load i18n %} and add "trans" right after the any
5. django-admin makemessages --locale=ko
6. add translated word into django.po
7. django-admin compilemessages

### deployment

1. pipenv install awsebcli --dev
2. eb init
3. mkdir .ebextensions
4. create django.config in .3
5. eb create "app title"

### static files

1. pipenv install django-storages
2. python manage.py collectstatic