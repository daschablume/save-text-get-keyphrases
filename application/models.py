#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""This module contains models for database.

Created on Fri Jan 22 15:35:56 2021

@author: macuser
"""

from application import db

'''
    Text and its key phrases are in two tables with relationships one-to-many.
    It's easy to get all the keyphrases with only one query;
    it's possible to know the correspondent text of any keyphrase
''' 

class Text(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), index=True)
    #the title of the article can be quite long, so (200) is there
    body = db.Column(db.String())
    keyphrases = db.relationship('KeyPhrase', backref='text', lazy='dynamic')

    def __repr__(self):
        return '<Text {}>'.format(self.name)    


class KeyPhrase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    text_id = db.Column(db.Integer, db.ForeignKey('text.id'))
    wiki_link = db.Column(db.String())

    def __repr__(self):
        return '<KeyPhrase {}>'.format(self.body)
    
    