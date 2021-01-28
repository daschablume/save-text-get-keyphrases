#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""This module contains models for database.
Created on Wed Jan 27 21:25:38 2021

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
    keyphrases = db.relationship('Keyphrase', backref='text', lazy='dynamic')

    def __repr__(self):
        return '<Text {}>'.format(self.title)    


class Keyphrase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    wiki_link = db.Column(db.String())
    counter = db.Column(db.Integer)
    text_id = db.Column(db.Integer, db.ForeignKey('text.id'))
    
    def __repr__(self):
        return '<Keyphrase {}>'.format(self.body)
    
    def increment_counter(self):
        self.counter += 1
        return self.counter
