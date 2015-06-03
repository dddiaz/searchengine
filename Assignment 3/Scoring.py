__author__ = 'Viral_Shah'

import math

def calculate_TF(frequency):
    if frequency == 0:
        return 0
    return 1+math.log10(frequency)

def calculate_IDF(corpus, document_frequency):
    return math.log10(float(corpus)/float(document_frequency))

def calculate_overall_score(termTF, location):
    if location == "title":
        return termTF*.6
    elif location == "text":
        return termTF*.3
    else:
        return termTF*.1