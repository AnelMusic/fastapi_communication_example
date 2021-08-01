#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 22:01:47 2021

@author: anelmusic
"""

from pydantic import BaseModel

class Location(BaseModel):
    continent: str
    capital: str
    