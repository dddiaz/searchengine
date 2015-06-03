__author__ = 'danieldiaz'
import pickle

class SearchResults:
    def __init__(self):
        self.results = {}
        self.search_phrase = ''
        self.term1 = None
        self.term2 = None
        self.termid1 = None
        self.termid2 = None
        self.search_size = 0
        self.term2termid = pickle.load( open( "/Users/danieldiaz/Desktop/PickleFiles/term2termID.pk", "rb" ) )
        self.term2tfidf = pickle.load(open("/Users/danieldiaz/Desktop/PickleFiles/term2TFIDF.pk","rb"))
        self.docid2url = pickle.load(open("/Users/danieldiaz/Desktop/PickleFiles/docID2URL.pk","rb"))

    def calcResults(self,search_phrase):
        self.search_phrase = search_phrase
        if (self.calcSearchLen() == 1):
            self.calc1gram()
        else:
            self.calc2gram()
        return self.constructResults()

    def calcSearchLen(self):
        if (len(self.search_phrase.split()) > 1):
            self.search_size = 2
            temp = self.search_phrase.split()
            self.term1 = temp[0]
            self.term2 = temp[1]
        else:
            self.search_size = 1
            self.term1 = self.search_phrase
        return self.search_size

    def calc1gram(self):
        self.termid1 = self.term_id_from_term(self.term1)
        if (self.termid1 is not None):
            self.finddocs(self.termid1)
        #check result is not none
        return

    def calc2gram(self):
        return

    def constructResults(self):
        self.results['search_phrase'] = self.search_phrase
        self.results['term_id1'] = self.termid1
        return self.results

    def term_id_from_term(self,term):
        try:
            term = term.lower();
            result = str(self.term2termid[term]);
        except:
            result = None
            #result = "term not found"
        return result

    def finddocs(self,termid):
        docs = self.term2tfidf[termid]
        firstdoc = docs[1]
        firstpage = self.docid2url[firstdoc]











# def return_query_results(search_phrase):
#     #init results dict
#     results = {};
#     term2termid = pickle.load( open( "/Users/danieldiaz/Desktop/PickleFiles/term2termID.pk", "rb" ) )
#     term2tfidf = pickle.load(open("/Users/danieldiaz/Desktop/PickleFiles/term2TFIDF.pk","rb"))
#     docid2url = pickle.load(open("/Users/danieldiaz/Desktop/PickleFiles/docID2URL.pk","rb"))
#
#     #figure out if 2 gram or single word
#     terms = search_phrase.split()
#     if (len(terms) == 1):
#         #do normal logic
#         z=1
#         #results = onegram(results,terms,)
#     else:
#         #its a 2gram...hopefully
#         z=1
#
#     results['search_phrase'] = search_phrase
#     results['term_id'] = term_id_from_term(search_phrase,term2termid)
#
#     return results
#
# def term_id_from_term(term,term2termid):
#     try:
#         term = term.lower();
#         #word_hash = pickle.load( open( "/Users/danieldiaz/Desktop/PickleFiles/term2termID.pk", "rb" ) )
#         result = str(term2termid[term]);
#     except:
#         result = "\nword not found\n"
#     return result