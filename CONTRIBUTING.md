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

# Amazon Cognito Set Up
Follow instructions on amazon for setting up a user pool.  This will include creating an app.

When setting up an app, outstanding questions:
 - Do you need to include Implicit Grant?  Currently, I did.
 - This URL should give you a token (in the URL): https://peopledepot.auth.us-east-2.amazoncognito.com/login?client_id=35ehknpgi8ul8nfn2undd6ufro&response_type=token&scope=openid&redirect_uri=http://localhost:8000/admin/

From chatgpt:
Step 1: Install Amplify CLI

The Amplify CLI (Command Line Interface) is a toolchain for building and managing AWS Amplify projects. You can install it globally using npm:

bash
Copy code
npm install -g @aws-amplify/cli
Step 2: Configure Amplify

After installing the Amplify CLI, you need to configure it to interact with your AWS account. Run the following command and follow the prompts:

bash
Copy code
amplify configure
This command will guide you through the AWS Amplify configuration process, including setting up your AWS IAM (Identity and Access Management) user, selecting your AWS region, and configuring the CLI with your AWS credentials.

Step 3: Create a New Amplify Project

Now, you can create a new AWS Amplify project in your React application directory:

bash
Copy code
amplify init
This command will prompt you to provide some information about your project, such as the project name, environment name, and default text editor. You can choose the default options for most of these prompts.

Step 4: Add Amplify Services

You can add Amplify services to your project based on your requirements. For example, to add authentication, you can run:

bash
Copy code
amplify add auth
This command will guide you through configuring authentication with Amazon Cognito. You can similarly add other services like API (for AWS AppSync), storage, and more using the amplify add command.

Step 5: Push Your Configuration

After adding services to your Amplify project, you need to push the configuration to your AWS account:

bash
Copy code
amplify push
This command will provision the necessary AWS resources and configure your backend services based on the Amplify configuration you specified.

Step 6: Integrate Amplify in Your React App

You will need to import and configure Amplify in your React application. Typically, this is done in your index.js or App.js file:

javascript
Copy code
import Amplify from 'aws-amplify';
import awsconfig from './aws-exports';

Amplify.configure(awsconfig);
Make sure to replace './aws-exports' with the correct path to your Amplify configuration file.

Step 7: Start Your React App

With Amplify configured, you can now start your React application:

bash
Copy code
npm start
Your React app will be running locally, and you can use Amplify services like authentication, storage, and APIs as needed within your application.

Remember that these steps provide a basic setup for using AWS Amplify in a React application. Depending on your project's requirements, you may need to add and configure additional services and adapt your code accordingly. Amplify offers various services for common cloud functionalities, and you can choose the ones that suit your project's needs.

Access Key AKIAZCDXVD2ZLX2H74X5
Secret Access Key i5d7lQd1LZnpB/v5Y9RUuJaqF9eLeqhJ4dkY+CjG

Add new models
Update urls
Copy personModel, personSerializer, personView

Many to Many
If relationship is meaningful then create a new model that includes both and use inLine.  Many to many method will let you select and deselect using Command-click.