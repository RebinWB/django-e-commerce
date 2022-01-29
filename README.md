# Django E-Commerce 
Simple E-Commerce using Django 4.0 for Back-End and DRF (Django Rest Framework) for APIs


# Installation
> this project is using PostgreSQL DataBase. so you must config your DataBase from **_./e_shop/settings.py/DATABASES_** before DB migrations. also you need install redis on your system, because we using redis DB for caching (config: **_./e_shop/settings.py/CACHES_**).
### install and create your virtual environment

install virtualenv:
```
pip install virtualenv
```

create virtual environment:
```
virtualenv venv
```

activate virtual environment:
```
cd venv\Scripts\activate
```

if you using Widows PowerShell, type this command in your PowerShell before activate virtual environment:
```
Set-ExecutionPolicy Unrestricted -Scope Process
```

### install requirements and run project

install requirements:
```
pip install -r requirements.txt
```

preparing DataBase:
```
python3 manage.py makemigrations
python3 manage.py migrate
```

create super user for access to admin section:
```
python3 manage.py createsuperuser
```
*fill necessary fields*

run project on localhost (default port: 8000):
```
python3 manage.py runserver <port>
```
