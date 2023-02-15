* `pip install django djangorestframework`

* `django-admin startproject <project_name> .` 

in my project :

`django-admin startproject music_controller .`

* Create App command: 
`django-admin startapp <app_name>`

I have Apps in my project:
1. api app `django-admin startapp api` to handle API. 
2. rest_framework `django-admin startapp rest_framework`

* Add the App I created to Project in sitting file.

* Update the DB

`python manage.py makemigrations`
`python manage.py migrate`

* To run the server
`python manage.py runserver`


