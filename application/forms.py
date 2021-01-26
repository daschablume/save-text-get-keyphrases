#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""This module contains fiels for flask form.

Created on Fri Jan 22 14:18:38 2021

@author: macuser
"""

from flask_wtf import FlaskForm
from wtforms import TextField, StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea


class TextForm(FlaskForm):
    ''' Use to create a form with a big text area and a small 
    field for the title of the text. 
    '''
    textfield = TextField(
        'Введіть текст сюди', widget=TextArea(), validators=[DataRequired()])
    titlefield = StringField('Назва тексту', validators=[DataRequired()])
    submit = SubmitField('Надіслати')
    