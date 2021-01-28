#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""This module contains logic to get a link from wikipedia.

Created on Mon Jan 25 20:47:33 2021

@author: macuser
"""

import wikipedia
import requests

def check_wiki(phrase): #takes an str and returns a str
    '''
    Search in wiki for a keyphrase and return a correspondent link.
    If there is an url, add to the result as well as disambiguation page.
    If there is no page with the correspondent name, return a string with
    information about it.
    '''
    try:
        page = wikipedia.page(phrase, auto_suggest=False)
        #if auto_suggest is True, it returns wrong result
        disambiguation_page = page.url + '_(disambiguation)'
        if requests.get(url=disambiguation_page).status_code == 404:
            result = page.url
        else:
            result = f'{page.url}.\n Також: {disambiguation_page}'
            
    except wikipedia.DisambiguationError:
        result = 'https://en.wikipedia.org/wiki/' + phrase + '_(disambiguation)'
    except wikipedia.PageError:
        result = 'На жаль, сторінки з таким іменем не існує.'
        
    return result




