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
TODO

## Run UI API (in our case localhost):
```
          $  python server_communication.py
```
Your output should look like:
TODO

## Creating new locations

http://worldtimeapi.org/api/timezone

