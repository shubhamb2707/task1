## Python version 3.6.8

## Create Virtual environment and install all the dependencies using following command
```
pip install -r requirements.txt
```

## Run Following commands to migrate models into db:
```
python manage.py migrate
```

## create admin user using following command : 
```
python manage.py createsuperuser
```

## Run Celery worker using following command : 
```
celery -A Task1 worker --pool=solo -l info
```

## Run server using following command : 
```
python manage.py runserver
```

To test the application follow these steps : 

open postman for testing all endpoints:
1)create user or signup user and if holiday will be there on that day so by the celery task all holiday of country will saved in the countryholidaytable
url:- http://127.0.0.1:8000/api/authentication/signup/
method :- POST 
Body data :- {
    "email":"joe@gmail.com",
    "password":"12345",
    "first_name":"joe",
    "last_name":"biden",
    "mobile":"2356895623"
    }
Note:- email and mobile no should be unique, email and password must be mandatory .

2)login user by email and password and get access token over there .
url :- http://127.0.0.1:8000/api/authentication/login/
method:- POST
Body data:- {
    "email":"joe@gmail.com",
    "password":"12345"
   
    }
Note ;- copy the access token and uuid from response data it will be usefull to authenticate other requests by brearer token 

3)create Post for like and unlike 
url:-http://127.0.0.1:8000/api/authentication/post/
method:-POST
get the uuid from login response and put into of_user of  body and access token put into brearer token 
Body data :- 
{
    "of_user":"10ac5b65-0c93-43c1-8604-bc1be6294ad0",
    "postdata":"Posting my first data "
   
    }

4)Getting all Post data 
put access token in bearer token, taken by login response 
url :-http://127.0.0.1:8000/api/authentication/post/
method:-GET
Body data :- empty 


5)Getting all User data 
put access token in bearer token, taken by login response 
url :-http://127.0.0.1:8000/api/authentication/allusers/
method:-GET
Body data :- empty 

6)like and unlike to Post 
put access token in bearer token, taken by login response 
url:- http://127.0.0.1:8000/api/authentication/likeunlike/
Method:-POST
Body data :-
"user_of" will be uuid of user taken from login response
"post_user" will be uuid of post taken all Get all Post response. 
{
    "user_of":"10ac5b65-0c93-43c1-8604-bc1be6294ad0",
    "post_user":"491c9e7c-d929-4088-8a2e-6abcae4acf61",
    "like":true,
    "unlike":false
   
    }
