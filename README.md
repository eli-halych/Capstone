# DSC Hackathon

## Motivation

The idea to implement such a platform emerged after joining Google Developers Group in Warsaw.
I though that would be great to organize something that would bring students closer together, 
promote technology in Warsaw communities and one of the ways to do so is to organize hackathons for students
and by students.

The students club would be called Developer Students Club and would unite many subgroups at a university club from different field,
directions, soft and hard skills, robotics, applications, databases, management and many more.

## Functionalities: roles, permissions and actions

The application should provide backend and frontend for a particular student club (DSC).

Such DSC would consist of members that would belong to either `lead` group or to `member` group. The `lead` group
inherits permissions from the `member` group.


###### DSC members permissions: <br>
    Can view a list of hackathons (short description)
    Can view a hackathon (full description)
    Can suggest (create) a hackathon
###### DSC leads permissions:
    DSC members' permissions and …
        Can delete a hackathon
        Can approve a hackathon
        Can update hackathon’s attributes
        
## Running the application

### The application is already hosted!

- Visit: https://dsc-hackathons.herokuapp.com/

- The main page will redirect you to the login page. The test users you can try are: <br> 
##### Member
```
    Login: member@member.com
    Password: member1!
```
##### Lead
```
    Login: lead@lead.com
    Password: leadmember1!
```
- After successful login, a JWT token will be generated in the URL line as access_token=`aaa.bbb.zzz` and you'll be redirected
to /hackathons. Don't worry if it says unauthorized! Frontend will come in future releases! Use test section below to try curl operations
which will provide authorized and protected access with the right JWT tokens!

- Now you can send requests to the backend.


### If you want to run it locally or on your server and set up your own Auth0:

- ##### Dependencies 
Dependencies are stored in requirements.txt which should be installed by running 

`pip install -r requirements`

- ##### Prepare database
Run to prepare necessary records:

```psql -U postgres dsc-hackathons < dsc-hackathons.pgsql```

- ##### Setup Auth0

1. Create a new Auth0 Account
2. Select a unique tenant domain
3. Create a new, single page web application
4. Create a new API
    - in API Settings:
        - Enable RBAC
        - Enable Add Permissions in the Access Token
5. Create new API permissions:
    - `get:hackathons`
    - `post:hackathons`
    - `patch:hackathons`
    - `put:hackathons`
    - `delete:hackathons`
6. Create new roles for:
    - Member
        - can `get:hackathons`
        - can `post:hackathons`
    - Lead
        - can `get:hackathons`
        - can `post:hackathons`
        - can `patch:hackathons`
        - can `put:hackathons`
        - can `delete:hackathons`
        
- ##### Set environment variables by running `setup.sh` with relevant values or doing it in your IDE:
```bash
#!/bin/bash

export FLASK_ENV=
export ALGORITHMS=[\'\']
export API_AUDIENCE=
export CLIENT_ID=
export REDIRECT_URL=
export JWT_SECRET=
export DATABASE_IRL=
```

## Documentaiton

- #### Endpoints
- #### Error handlers

- ###### When are errors expected
- ###### Endpoint description

- #### Sending requests
- #### Tests requests

- #### Database structure
