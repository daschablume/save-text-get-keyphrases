#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""This module gets key phrases from a text. It follows the approach
of Florian Boudin (http://aclweb.org/anthology/C16-2015) and uses his
package.

Created on Mon Jan 25 18:31:29 2021

"""
import pke
keyphrase_number = 6 #it seems to be a relevant numbeer for a research

def get_keyphrases(text):
    # initialize keyphrase extraction model, here TopicRank
    extractor = pke.unsupervised.TopicRank()
    
    # load the content of the document, here document is expected to be in raw
    # format (i.e. a simple text file) and preprocessing is carried out using spacy
    extractor.load_document(text, language='en')
    
    # keyphrase candidate selection, in the case of TopicRank: sequences of nouns
    # and adjectives (i.e. `(Noun|Adj)*`)
    extractor.candidate_selection()
    
    # candidate weighting, in the case of TopicRank: using a random walk algorithm
    extractor.candidate_weighting()
    
    # N-best selection, keyphrases contains the 10 highest scored candidates as
    # (keyphrase, score) tuples
    keyphrases = extractor.get_n_best(n=keyphrase_number)
    
    #return only keyphrases without their frequencies
    keyphrases_list = [i[0] for i in keyphrases]
    
    return keyphrases_list

