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

`pip install -r requirements.txt`

- ##### Prepare database
Run to prepare necessary records:

```psql -U postgres dsc-hackathons < dsc-hackathons.pgsql```
It is ok, if it shows some violation errors, since after running a Flask instance, Flask will create the database
and besides adding rows to the database the dumped file will try to recreate the database. It should insert only statuses.

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

- #### Status pairs
DSC lead can change the status of a hackathon after it was posted
```
status_id: 1 | name: Pending
status_id: 2 | name: Approved
status_id: 3 | name: Rejected
```

- #### Endpoints
```
1. GET /hackathons
2. POST /hackathons
3. GET /hackathons/<hackathon_id>
4. PATCH /hackathons/<hackathon_id>
5. PUT /hackathons/<hackathon_id>
5. DELETE /hackathons/<hackathon_id>
```

- #### Error handlers
```
1. 400 - Bad Request
2. 401 - Unauthorized
3. 403 - Forbidden
4. 404 - Not Found
5. 422 - Unprocessable Entity
```

- ###### When are errors expected
```
1. 400 - Request body is malformed
2. 401 - JWT cannot be verified or Authorization header is invalid
3. 403 - No permission in JWT to access an endpoint
4. 404 - Requested resource is not found
5. 422 - Request fails to succeed
```

- ###### Endpoint description
```
1. GET /hackathons
    - Returns a list of all ahckathons in short representation.
    - Request Body: None
    - Request Parameters: None 
    - Identifiers: None
    - Expected Errors: 404
    - Expected Permission: get:hackathons
    - Return Body: a list of short representations of hackathons and a success status
    {
      "hackathons": [
        {
          "end_time": "Sun, 21 Jan 2001 00:00:00 GMT",
          "id": 1,
          "name": "Cloud Technologies Hackathon",
          "place_name": "Google Campus",
          "start_time": "Thu, 11 Jan 2001 00:00:00 GMT"
        }
      ],
      "success": true
    }    
```

```
2. POST /hackathons
    - Creates a hackthons with given parameters in the request body.
    - Request Body: 
    {
      "name": "Cloud Technologies Hackathon",
      "start_time": "2001-01-11T00:00:00",
      "end_time": "2001-01-21T00:00:00",
      "place_name": "Google Campus",
      "status_id": 1
    }
    - Request Parameters: None 
    - Identifiers: None
    - Expected Errors: 400, 422
    - Expected Permission: post:hackathons
    - Return Body: the newly created hackathon's ID and a success status
    {
      "hackathon_id": 1,
      "success": true
    }
```

```
3. GET /hackathons/<id_hackathon>
    - Load a full representation of a hackathon.
    - Request Body: None
    - Request Parameters: None 
    - Identifiers: id_hackathon
    - Expected Errors: 400, 404, 422
    - Expected Permission: get:hackathons
    - Return Body: a full representation of a hackathon, the hackathon's ID and a success status
    {
      "hackathon": {
        "end_time": "Sun, 21 Jan 2001 00:00:00 GMT",
        "id": 1,
        "name": "Google Cloud Technologies",
        "place_name": "Google Campus",
        "start_time": "Thu, 11 Jan 2001 00:00:00 GMT",
        "status_id": 1
      },
      "hackathon_id": 1,
      "success": true
    }    
```

```
4. PATCH /hackathons/<id_hackathon>
    - Changes hackathon's status to approved/rejected/pending. This example changes Pending to Approved (status_id from 1 to 2).
    - Request Body:
    {
      "status_id": 2
    }
    - Request Parameters: None 
    - Identifiers: id_hackathon
    - Expected Errors: 400, 404, 422
    - Expected Permission: patch:hackathons
    - Return Body: a full representation of a hackathon, the hackathon's ID, the newsly updated status name and a success status
    {
      "hackathon": {
        "end_time": "Sun, 21 Jan 2001 00:00:00 GMT",
        "id": 1,
        "name": "Google Cloud Technologies",
        "place_name": "Google Campus",
        "start_time": "Thu, 11 Jan 2001 00:00:00 GMT",
        "status_id": 2
      },
      "hackathon_id": 1,
      "status": "Approved",
      "success": true
    } 
```

```
5. PUT /hackathons/<id_hackathon>
    - Updates the whole representation of a hackathon.
    - Request Body:
    {
      "name": "Google Cloud Technologies Changed",
      "start_time": "2001-01-12T00:00:00",
      "end_time": "2001-01-22T00:00:00",
      "place_name": "Google Campus Changed"
    }
    - Request Parameters: None 
    - Identifiers: id_hackathon
    - Expected Errors: 400, 404, 422
    - Expected Permission: put:hackathons
    - Return Body: a full representation of the updated hackathon, the hackathon's ID and a success status
    {
      "hackathon": {
        "end_time": "Mon, 22 Jan 2001 00:00:00 GMT",
        "id": 1,
        "name": "Google Cloud Technologies Changed",
        "place_name": "Google Campus Changed",
        "start_time": "Fri, 12 Jan 2001 00:00:00 GMT",
        "status_id": 2
      },
      "hackathon_id": 1,
      "success": true
    }
```

```
6. DELETE /hackathons/<id_hackathon>
    - Removes the hackathon fully.
    - Request Body: None
    - Request Parameters: None 
    - Identifiers: id_hackathon
    - Expected Errors: 400, 404, 422
    - Expected Permission: delete:hackathons
    - Return Body: removed hackathon's ID and a success status
    {
      "hackathon_id": 1,
      "success": true
    }
```

- #### Sending requests
##### NOTE: get the JWT token after successful login as a member of a lead. 
##### Include your JWT token in the authorization header. After the POST request the ID of a new hackathon you can also use will be returned.

Run [`./this_collection.json`](https://github.com/eli-halych/DSC-Hackathons/blob/master/DSC-Hackathons.postman_collection.json) in Postman.
