#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: anelmusic
"""

import requests
import location

URL = 'http://127.0.0.1:8000/' # localhost

def start_menue():
    """Creates console UI"""
    while True:
        print('\n\n<0> Add new location to Database')
        print('<1> GET all location times ')
        print('<2> GET specific location time by ID')
        print('<3> Delete specific location by ID')
        print('<4> Exit')
        option = input("\nInput: ")
        if option == '4':
            break

        if option == '0':
            new_continent = input("Continent: ")
            new_capital = input("Capital: ")
            myobj = location.Location(continent = new_continent, capital = new_capital).dict()
            try:
                request = requests.post(URL+'locations', json=myobj)
                request.raise_for_status()
            except requests.exceptions.HTTPError as err:
                raise SystemExit(err) from err
        elif option == '1':
            try:
                request = requests.get(URL+'locations')
                request.raise_for_status()
                print("Server Response: ", request.text)
            except requests.exceptions.HTTPError as err:
                raise SystemExit(err) from err
        elif option == '2':
            location_id = input("Location ID: ")
            try:
                request = requests.get(URL+'locations'+'/'+location_id)
                request.raise_for_status()
                print("Server Response: ", request.text)
            except requests.exceptions.HTTPError as err:
                raise SystemExit(err) from err
        elif option == '3':
            location_id = input("Location ID: ")
            try:
                request = requests.delete(URL+'locations'+'/'+location_id)
                request.raise_for_status()
                print("Server Response: ", request.text)
            except requests.exceptions.HTTPError as err:
                raise SystemExit(err) from err
        else:
            print("Invalid Input")

if __name__ == '__main__':
    start_menue()
