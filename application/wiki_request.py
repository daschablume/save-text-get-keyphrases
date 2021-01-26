#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""This module contains logic to get a link from wikipedia.

Created on Mon Jan 25 20:47:33 2021

@author: macuser
"""

import wikipediaapi

wiki_wiki = wikipediaapi.Wikipedia('en')

def check_wiki(keyphrases):
    '''
    Search in wiki for each key phrase; if there is no page with the 
    correspondent name, return None.
    '''
    links = {}
    for phrase in keyphrases:
        page = wiki_wiki.page(phrase)
        try:
            links[phrase] = page.canonicalurl
        except KeyError: #if page doesn't exist 
            links[phrase] = None
    return links
    