<style>
table, th, td {
  border: 3px solid;
}
th {
  font-weight: normal;
}
</style>

# Background
I added rest_framework and imported token to try to build a token screen screen.  I found out there is a built in view and template that lets you do that.  To get tokens to work, I had to:
- `python3 manage.py makemigrations rest_framework.auth_token`  


Keys
- Cog - 35ehknpgi8ul8nfn2undd6ufro
- Google - 

Summary
- SRA - Client calls express/passportjs backend to help authenticate with google.  User info passed from backend to client with /auth/user route.
- SOC - Django app integrated with single sign on using allauth and social accounts.  Rest framework without authorization implemented.  Configured for Amazon Cognito.

- [ ] **Update Status**
  - [x] SRA - compare to github and review code
  - [x] SRA - update summary and CONTRIBUTING.md
  - [X] SOC - update summary and CONTRIBUTING.md
  - [x] PPD - understand how APIs auto generated, document in CONTRIBUTING.md and summary

- [ ] **SRA gets list of all accounts in SOC if role SRA_MAINTAINER from frontend**
  - [ ] SOC - add view accounts to SRA_MAINTAINER
  - [ ] SRA - create screen to display accounts

- [ ] **SRA gets list of all accounts in SOC if role SRA_MAINTAINER from frontend**
  - [ ] SOC - add view accounts to SRA_MAINTAINER
  - [ ] SRA - create screen to display accounts

- [ ] **SRA/SOC display movies if logged in**
  - [ ] Add movies and people
  - [ ] Understand better InLine and Admin, particularly ["name"]
  - [X] Copy JWT code
  - [ ] Remove JWT code
  - [ ] Get token manually (see CONTRIBUtiNG from peopledepot)
  - [ ] Try token to see if API gives permissions
  - [ ] Look at code for getting token
  - [ ] Add API for getting profile and movies
  
- [ ] **SRA display token**
  - [ ] Display token after login https://stackoverflow.com/questions/64991155/how-do-i-get-a-token-from-django-allauth-socialaccount


- [ ] **View technologies in SOC if role SRA_MAINTAINER**
  - [ ] SOC - Create technologies table
  - [ ] SOC - Associate SRA_MAINTAINER role with view SRA_MAINTAINER

**Restrict SRA update to technologies that begin with the letter "G"**
- [ ] SOC - Associate SRA_MAINTAINER with update technology
- [ ] SOC - Test **direct** update technology API
- [ ] SRA - Add update technology API to SRA server
- [ ] SOC - disallow unless it comes from SRA server
- [ ] SRA - Add screen for updating technology

**Restrict SRA update technologies to those in ALLOWED_TECHNOLOGIES**
- [ ] SRA - Create ALLOWED_TECHNOLOGIES and API that is a list of SOC technologies
- [ ] SRA - Allow view and update if role SRA_ADMIN
- [ ] SRA - Modify update technologies to look at ALLOWED_TECHNOLOGIES

**Other Epics**
- KB - create API for initial replication of technologies from PD and restrict to role KB_ADMIN
- KB - create API for update of users if role KB_ADMIN
- PD - restrict update of user if not come from KB server

# socialaccount
- [ ] * Update/verify current status in CONTRIBUTING.md and summary here
- [ ] * Generate APIs for users and roles
- [ ] Implement token screen.  See [link](https://stackoverflow.com/questions/14838128/django-rest-framework-token-authentication)
- [ ] Try adding google account
- [ ] Try adding google account to cognito
- [ ] Create technologies table
- [ ] Rename socialaccount-django-admin-allauth
- [ ] Consider using husky
- [ ] Figure out why signup requires manually confirming

# peopledepot
- [ ] Understand how APIs generated
- [ ] Try URL for login to get token
- [ ] Modify instructions based on token and above
- [ ] Implement SSO screen in PeopleDepot using steps done in CONTRIBUTING.md of socialaccount (this project).
- [ ] Consider using husky

# sample-react-app
- [x] Enter missing code from github
- [ ] Compare to existing code from github
- [ ] Understand code
- [ ] Document status with no account, account, and intended privilege "SREA_MAINTAINER" as summary and in CONTRIBUTING
- [ ] Add Cognito as an option for logging in
- [ ] Rename sample-react-app => sample-react-express-app
- [ ] Consider using husky

# knowledgebase
- [ ] Fix many to many so refer to table
- [ ] Take learnings from above
  - [ ] Implement sso for cognito
- [ ] Consider using husky
