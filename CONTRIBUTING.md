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
django-admin startproject ethanproject
cd ethanproject
python3 manage.py startapp ethanapp
https://django-allauth.readthedocs.io/en/latest/installation/quickstart.html

Follow instructions in https://django-allauth.readthedocs.io/en/latest/installation/quickstart.html
    pip install allauth
    Make file changes
    Watch out for duplicate entries, especially in INSTALLED_APPS
    python3 manage.py migrate
9:30

If you get a message about duplicate when you log in, try removing entry from settings.py if you specified credential info in that file.

Register google (https://django-allauth.readthedocs.io/en/latest/socialaccount/providers/google.html)
22:00


