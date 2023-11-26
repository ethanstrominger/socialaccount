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
python -m pip install django
python -m pip install psycopg2==2.7.4
django-admin startproject ethanproject
cd ethanproject
python3 manage.py createsuperuser
python3 manage.py startapp ethanapp
python3 -m pip install load_dotenv

import dotenv
dotenv.load_dotenv()

Create .env file
DEBUG = 1
SECRET_KEY = foo3
COGNITO_AWS_REGION=us-east-2
COGNITO_USER_POOL=us-east-2_i2EKGBFG1
COGNITO_CLIENT_ID=35ehknpgi8ul8nfn2undd6ufro
COGNITO_DOMAIN=peopledepot
COGNITO_URL=f'https://{COGNITO_DOMAIN}/auth.{COGNITO_AWS_REGION}.amazoncognito.com'

In settings.py:

COGNITO_AWS_REGION = os.environ.get("COGNITO_AWS_REGION", default=None)
COGNITO_USER_POOL = os.environ.get("COGNITO_USER_POOL", default=None)
COGNITO_AWS_REGION = os.environ.get("COGNITO_AWS_REGION", default=None)
COGNITO_CLIENT_ID = os.environ.get("COGNITO_CLIENT_ID", default=None)
COGNITO_CLIENT_SECRET = os.environ.get("COGNITO_CLIENT_SECRET", default=None)
COGNITO_DOMAIN=os.environ.get("COGNITO_DOMAIN", default=None)
COGNITO_URL=os.environ.get("COGNITO_URL", default=None)


Follow instructions in https://django-allauth.readthedocs.io/en/latest/installation/quickstart.html with following exceptions: 
  - change `pip install django-allauth` to `python3 -m pip install django-allauth`
  - for SOCIALACCOUNT_PROVIDERS, do not hard code in values in settings.py.  Here is an example of how you could do that:

  SOCIALACCOUNT_PROVIDERS = {
    'amazon_cognito': {
        'DOMAIN': f'{COGNITO_URL}',
        'APP': {
            'client_id': f'{COGNITO_CLIENT_ID}',
            'client_secret': f'{COGNITO_CLIENT_SECRET}',
            'secret': '',
            'key': ''
        }
    }
}

- Follow instructions in https://docs.allauth.org/en/latest/socialaccount/providers/index.html

- Modify settings.py.  Change ALLOWED_HOSTS=[] to ALLOWED_HOSTS=["localhost"]
- python3 manage.py runserver


```
LOGIN_REDIRECT_URL = '/admin/'
ACCOUNT_LOGOUT_REDIRECT_URL = 'account_login'
```

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
- create templates/socialaccount directory
- create authorization_error.html:
```
Single signon error.  Inform the admin.  Detail error:

{{ authorization_error }}
```
- Instructions on how to change admin
- Figure out how to continue to original URL
- Make for a prettier log in screen
- tokens url





WIP: Tokens view.  I added token view to make it easier to get token so I could display it on the screen.  I found out there is a built in view and template that lets you do that.  To get tokens to work, I had to:
- `python3 manage.py makemigrations rest_framework.auth_token`  
See https://stackoverflow.com/questions/14838128/django-rest-framework-token-authentication step 7.

# Add new models
Update urls
Copy personModel, personSerializer, personView

# Activating env
./create-env.sh (will create <$PWD>-venv env)
source ./activate.sh (will activate $PWD-venv env)
# Many to Many 
If relationship is meaningful then create a new model that includes both and use inLine.  Many to many method will let you select and deselect using Command-click.

# Amazon Cognito Set Up
Follow instructions on amazon for setting up a user pool.  This will include creating an app.

- Create user pool
- Create an app
  - Select option to generate client secret key for extra security
  - Enter into Allowed callback URLs
  ```
  localhost:8000/amazon-cognito/login/callback/
  localhost:8000/admin
  ```
  - Enter into Allowed sign-out URLs 
  ```
  https://localhost:8000/admin/signout
  ```
  