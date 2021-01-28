#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""This module creates endpoints for two pages

Created on Fri Jan 22 13:37:15 2021

@author: macuser
"""
from flask import render_template, flash, redirect, url_for
from application import app, db
from application.forms import TextForm
from application.models import Text, Keyphrase
import application.find_keyphrases_alternative as find_keyphrases
import application.wiki_request as wiki
from operator import itemgetter


@app.route('/', methods=['GET', 'POST'])
def upload_text():
    '''
    Get text, find its keyphrases, search for each keyphrase in wiki
    and then commits text to the 'text' column in the database, and key phrases
    with corresponding wiki links to the 'keyphrase' column in the database.
    To avoid duplicates in DB and for the sake of fast querying each keyphrase
    has 'counter' column.
    '''
    form = TextForm()
    if form.validate_on_submit():
        text = Text(title=form.titlefield.data, body=form.textfield.data)
        keyphrases = find_keyphrases.get_keyphrases(form.textfield.data)
        for phrase in keyphrases:
            #check if keyphrase is already in DB; if so, increment its counter
            keyphrase = Keyphrase.query.filter_by(body=phrase).first()
            if keyphrase:
                keyphrase.increment_counter()
            else:
                keyphrase = Keyphrase(
                    body=phrase, counter=0, wiki_link=wiki.check_wiki(phrase)
                                    )               
                text.keyphrases.append(keyphrase)
                db.session.add(keyphrase)
        db.session.add(text)
        db.session.commit()
        flash('Вітаємо, ви завантажили текст')
        return redirect(url_for('upload_text'))
    return render_template('upload_text.html', form=form)



@app.route('/top_keyphrases', methods=['GET'])
def top_keyphrases():
    '''
    Query DB for all the keyphrases, sort them by their counter and
    then return top-7 of them ('7' here is an arbitrary number)
    '''
    number_of_top_phrases = 7
    query = db.session.query(Keyphrase).order_by(
        Keyphrase.counter.desc()).limit(number_of_top_phrases).all()
    return render_template('top_keyphrases.html', top_phrases=query)




    