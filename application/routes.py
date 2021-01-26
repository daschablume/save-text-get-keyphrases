#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""This module creates endpoints for two pages

Created on Fri Jan 22 13:37:15 2021

@author: macuser
"""
from flask import render_template, flash, redirect, url_for
from application import app, db
from application.forms import TextForm
from application.models import Text, KeyPhrase
import application.find_keyphrases_alternative as find_keyphrases
import application.wiki_request as wiki
from operator import itemgetter


@app.route('/', methods=['GET', 'POST'])
def upload_text():
    '''
    Get text, find its key phrases, search for each key phrase in wiki
    and then commits text to the 'text' column in the database, and key phrases
    with corresponding wiki links to the 'key_phrase column in the database'
    '''
    form = TextForm()
    if form.validate_on_submit():
        text = Text(title=form.titlefield.data, body=form.textfield.data)
        keyphrases = find_keyphrases.get_keyphrases(form.textfield.data)
        keyphrases_links_dict = wiki.check_wiki(keyphrases)
        for key in keyphrases_links_dict:
            keyphrase = KeyPhrase(
                body=key, wiki_link=keyphrases_links_dict[key])
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
    Query DB for all the key phrases, sort them by their frequency and
    then return top-7 of them ('7' here is an arbitrary number)
    '''
    number_of_top_phrases = 7
    all_phrases_obj = KeyPhrase.query.all()
    all_phrases_bodies = [i.body for i in all_phrases_obj]
    all_phrases_dict = {}
    for i in all_phrases_bodies:
        if i in all_phrases_dict.keys():
            all_phrases_dict[i] += 1
        else:
            all_phrases_dict.update({i: 1})
    sorted_phrases = sorted(
        all_phrases_dict.items(), key=itemgetter(1), reverse=True)
    #sorted_phrases is a list of tuples, so =>
    top_phrases = [i[0] for i in sorted_phrases[:number_of_top_phrases]]
    
    return render_template('top_keyphrases.html', top_phrases=top_phrases)
    