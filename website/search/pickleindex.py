__author__ = 'danieldiaz'
import pickle

def term_id_from_term(term):
    try:
        term = term.lower();
        word_hash = pickle.load( open( "/Users/danieldiaz/Desktop/PickleFiles/word_hash.pk", "rb" ) )
        result = str(word_hash[term]);
    except:
        result = "word not found"
    return result