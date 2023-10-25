Resources:

- https://python.plainenglish.io/proper-way-of-using-google-authentication-with-django-and-django-allauth-part-2-c47b87dd1283
- https://python.plainenglish.io/proper-way-of-using-google-authentication-with-django-and-django-allauth-b77f429e3f5d
- youtube https://www.youtube.com/watch?v=GQySb3W2feo
- https://docs.djangoproject.com/en/4.2/topics/auth/default/
- https://www.google.com/search?q=multiple+django+admin+apps+single+authorization
- https://www.w3schools.com/django/django_template_variables.php


python3 -m venv venv
source venv/bin/activate (or source ./activate.sh)
Add venv to .gitignore
pip install django
django-admin startproject ethanproject
cd ethanproject
python3 manage.py createsuperuser
python3 manage.py startapp ethanapp
https://django-allauth.readthedocs.io/en/latest/installation/quickstart.html

- youtube https://www.youtube.com/watch?v=GQySb3W2feo
Time: 0
Demo of app that will be bult
Time 6:00
Goes through instructions below

Follow instructions in https://django-allauth.readthedocs.io/en/latest/installation/quickstart.html
    pip install django-allauth
    Make file changes
    Watch out for duplicate entries, especially in INSTALLED_APPS
    python3 manage.py migrate

9:50
- Modify settings.py.  Change ALLOWED_HOSTS=[] to ALLOWED_HOSTS=["localhost"]
- python3 manage.py runserver
Ignore "site_id" comments

11:50
Follow instructions in https://docs.allauth.org/en/latest/socialaccount/providers/index.html

18:30
Adding data to SOCIAL APPS, SOCIAL ACCOUNTS can skip

21:33 - Google login screen now avaible.  Redirects to profile
How to change redirect and create a page
- add REDIRECT_URL="home/" to settings.py
- add this to TEMPLATES section of settings.py:

```
'DIRS': [os.path.join(BASE_DIR,'templates')]
```

- add this to URLS.py
```
from django.views.generic import TemplateView
    <!-- next to other path  statements -->
    path('home/', TemplateView.as_view(template_name='common/home.html'), name='home'),

```






If you get a message about duplicate when you log in, try removing entry from settings.py if you specified credential info in that file.

Register google (https://django-allauth.readthedocs.io/en/latest/socialaccount/providers/google.html)
22:00

WIP: Tokens view.  I added token view to make it easier to get token so I could display it on the screen.  I found out there is a built in view and template that lets you do that.  To get tokens to work, I had to:
- `python3 manage.py makemigrations rest_framework.auth_token`  
See https://stackoverflow.com/questions/14838128/django-rest-framework-token-authentication step 7.

Change to read vars from .env

# Amazon Cognito Set Up
Follow instructions on amazon for setting up a user pool.  This will include creating an app.

When setting up an app, outstanding questions:
 - Do you need to include Implicit Grant?  Currently, I did.
 - This URL should give you a token (in the URL): https://peopledepot.auth.us-east-2.amazoncognito.com/login?client_id=35ehknpgi8ul8nfn2undd6ufro&response_type=token&scope=openid&redirect_uri=http://localhost:8000/admin/

# Add new models
Update urls
Copy personModel, personSerializer, personView

# Many to Many
If relationship is meaningful then create a new model that includes both and use inLine.  Many to many method will let you select and deselect using Command-click.