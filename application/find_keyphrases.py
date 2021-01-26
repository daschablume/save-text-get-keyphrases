#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 12:18:24 2021

@author: macuser
"""
from operator import itemgetter
import math
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize 
import re

stop_words = set(stopwords.words('english'))
keyword_number = 6 #it seems to be a relevant number for a research

def text_processing(text):
    
    #get number of sentences to calculate IDF
    total_sentences = sent_tokenize(text)
    total_sent_len = len(total_sentences)
    
    #clean the text from symbols, numbers and stop_words; 
    #get list of words for calculation of TF
    pattern = r'[^\w]'
    text = re.sub(pattern, ' ', text)
    pattern = r'\d+'
    text = re.sub(pattern, ' ', text)
    total_words = word_tokenize(text.lower())
    total_words = [w for w in total_words if not w in stop_words]
    total_word_length = len(total_words)
    
    
    #calculate term frequency for each word and add it to dict
    tf_score = {}
    for each_word in total_words:
        if len(each_word) > 1:
            if each_word in tf_score:
                tf_score[each_word] += 1
            else:
                tf_score[each_word] = 1
    
    # Dividing by total_word_length for each dictionary element
    tf_score = {x: y/total_word_length for x, y in tf_score.items()}


    # if the word present in a sentence list; to calculate IDF
    def check_sent(word, sentences): 
        final = [all([w in x for w in word]) for x in sentences] 
        sent_len = [sentences[i] for i in range(0, len(final)) if final[i]]
        return len(sent_len)
    
    #calculate IDF
    idf_score = {}
    for each_word in total_words:
            if each_word in idf_score:
                idf_score[each_word] = check_sent(each_word, total_sentences)
            else:
                idf_score[each_word] = 1
                            
    for x in idf_score:
        try: 
            idf_score[x] = math.log(total_sent_len/idf_score[x])
        except ZeroDivisionError:
            pass
        
    #keys in both dicts are the same; multiply values iterating only one dict
    tf_idf_score = {key: tf_score[key] * idf_score[key] for key in tf_score.keys()}
    
    #func to get important words in the doc: sort from the highest value
    def get_top_n(dict_elem, n):
        result = dict(sorted(dict_elem.items(), key = itemgetter(1), reverse = True)[:n]) 
        return result
    
    result = (get_top_n(tf_idf_score, keyword_number)).keys()
    return result
