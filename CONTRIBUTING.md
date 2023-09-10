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
Register google (https://django-allauth.readthedocs.io/en/latest/socialaccount/providers/google.html)


