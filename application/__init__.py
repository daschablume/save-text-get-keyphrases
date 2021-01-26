#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 13:33:16 2021

@author: macuser
"""

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from application import routes, models