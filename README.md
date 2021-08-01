[![Travis](https://img.shields.io/badge/language-Python-red.svg)]()
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)


# FastAPI Toyexample
This project is used to illustrate the convenient usage of fastAPI. In this project we will a local (in memory) database to store a location object.
Using a REST API we can access the database information aswelle as create and store location objects.

## Prerequisite:
##### Installation:
```
        Python3.6+:
         	$  pip install fastapi
          $  pip install uvicorn[standard]
```
     
## Start Server API (in our case localhost):
Hint: --reload makes the server restart after code changes. Only do this for development.
```
          $  uvicorn timezone_api:app --reload...
```
Your output should look like:

![start_server](https://user-images.githubusercontent.com/32487291/127780680-177ca54f-5d4d-4319-af5e-7b3fa90ab48e.png)

## Run UI API (in our case localhost):
```
          $  python server_communication.py
```
Your output should look like:

![server_communication](https://user-images.githubusercontent.com/32487291/127780664-b4bc0f68-6bed-477e-8a94-bc1b9b459e29.png)

## Creating new locations
To add new locations to the database select option 0.
You can find all available locations here: http://worldtimeapi.org/api/timezone

The worldtimeapi is utilized by our RestAPI to get the coresponding date and time information.

## Testing the API without the local server_communication.py:
You can access the interactive dynamic API documentation here: http://127.0.0.1:8000/docs

![api_docs](https://user-images.githubusercontent.com/32487291/127780858-95a73dc1-a321-4c11-976f-8470bef9628b.png)




