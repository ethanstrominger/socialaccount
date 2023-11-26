https://django-allauth.readthedocs.io/en/latest/installation/quickstart.html

- youtube https://www.youtube.com/watch?v=GQySb3W2feo
Time: 0
Demo of app that will be bult
Time 6:00
Goes through instructions below

Follow instructions in https://django-allauth.readthedocs.io/en/latest/installation/quickstart.html with following exceptions: 
  - change `pip install django-allauth` to `python3 -m pip install django-allauth`
  - for each auth provider, add to social accounts table rather than config
Here is a summary of the steps:

    python3 -m pip install django-allauth
    Make file changes as indicated in the article
    python3 manage.py migrate

SOCIALACCOUNT_PROVIDERS = {
    'amazon_cognito': {
        'DOMAIN': 'https://peopledepot.auth.us-east-2.amazoncognito.com',
        'APP': {
            'client_id': f'{COGNITO_CLIENT_ID}',
            'client_secret': f'{COGNITO_CLIENT_SECRET}',
            'secret': '',
            'key': ''
        }
    }
}
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
- add to settings.py
```
LOGIN_REDIRECT_URL = 'home'
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






If you get a message about duplicate when you log in, try removing entry from settings.py if you specified credential info in that file.

Register google (https://django-allauth.readthedocs.io/en/latest/socialaccount/providers/google.html)
22:00

WIP: Tokens view.  I added token view to make it easier to get token so I could display it on the screen.  I found out there is a built in view and template that lets you do that.  To get tokens to work, I had to:
- `python3 manage.py makemigrations rest_framework.auth_token`  
See https://stackoverflow.com/questions/14838128/django-rest-framework-token-authentication step 7.

