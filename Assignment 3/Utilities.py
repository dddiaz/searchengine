__author__ = 'Viral_Shah'

import nltk


def parser(file_text):
     tokens = nltk.word_tokenize(file_text)
     revised = [token.lower() for token in tokens if token.isalnum()]
     return revised

def frequency_counter(tokens):
    fd = nltk.FreqDist(tokens)
    return fd
