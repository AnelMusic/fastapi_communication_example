#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 23:03:55 2021
@author: anelmusic

We will use paths in this tutorial
paths = called endpoints or route
Here, we can see the fastAPI magic
Using type hints we can tell which types to expect in
order to work
In other frameworks such as Flask you have to do
a lot of additional steps to make this work
"""
from datetime import datetime

import json
import requests

from fastapi import FastAPI
import location


URL = 'http://127.0.0.1:8000/' # localhost

app = FastAPI()

# In memory database
# Typically this would be some remote DB
timezone_database = []


@app.get('/')
def index():
    """Return the todo"""
    return "Use: URL/docs to access API documentation"

@app.get('/locations')
def get_locationtimes():
    """Returns locations and respective timedate information"""
    timezone_infos = []
    if not timezone_database:
        return 'Database empty'

    for timezone in timezone_database:
        info_msg = get_infomessage(timezone)
        timezone_infos.append(info_msg)
    return timezone_infos

@app.get('/locations/{location_id}')
def get_locationtime(location_id: int):
    """Returns specific location and respective timedate information"""
    if not timezone_database:
        return 'Database empty'
    if 1 <= location_id <= len(timezone_database):
        info_msg = get_infomessage(timezone_database[location_id-1])
        return info_msg
    return f'location_id must be >= 1 and <= {len(timezone_database)}'


@app.post('/locations')
def create_location(timezone: location.Location):
    """Adds new timezone to database and returns info message"""
    timezone_database.append(timezone)
    return f'Created {timezone.continent}/{timezone.capital}'

@app.delete('/locations/{location_id}')
def delete_location(location_id: int):
    """Removes specific timezone from database and returns info message"""
    if not timezone_database:
        return 'Database empty'
    if 1 <= location_id <= len(timezone_database):
        continent = timezone_database[location_id-1].continent
        capital = timezone_database[location_id-1].capital
        timezone_database.pop(location_id-1)
        return f'Removed id: {location_id} - {continent}/{capital}'
    return f'location_id must be >= 1 and <= {len(timezone_database)}'

def get_infomessage(timezone):
    """Return special timezone string representation"""
    try:
        request = requests.get('http://worldtimeapi.org/api/timezone/'
                               +f'{timezone.continent}/{timezone.capital}')
        request.raise_for_status()
        request_data = json.loads(request.text)
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err) from err
    # Datetime Format: 2021-07-31T23:32:41.870104+02:00
    datetime_info = request_data["datetime"]
    datetime_object = datetime.strptime(datetime_info, "%Y-%m-%dT%H:%M:%S.%f%z")
    current_date = datetime_object.strftime("%d-%m-%Y")
    current_time = datetime_object.strftime("%H:%M:%S")
    info_msg = (f'{timezone.continent}/{timezone.capital}'
                +f' - Date:{current_date} - Current Time: {current_time}')
    return info_msg

def check_connection(url):
    """Checks if HOST is available and raises error if HOST is down"""
    try:
        request = requests.get(url)
        request.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err) from err

def main():
    """Raises SystemExit in case Host is not reachable"""
    check_connection(URL)

if __name__ == '__main__':
    main()
    