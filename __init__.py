#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 08:53:35 2018

@author: kdg
"""

from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from AppCamera import routes





