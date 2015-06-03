__author__ = 'danieldiaz'
import pickle
import operator

class SearchResults:
    def __init__(self):
        self.results = {}
        self.maxResults = 10
        self.search_phrase = ''
        self.term1 = None
        self.term2 = None
        self.termid1 = None
        self.termid2 = None
        self.search_size = 0
        self.term2termid = pickle.load( open( "/Users/danieldiaz/Desktop/PickleFiles/term2termID.pk", "rb" ) )
        self.term2tfidf = pickle.load(open("/Users/danieldiaz/Desktop/PickleFiles/term2TFIDF.pk","rb"))
        self.docid2url = pickle.load(open("/Users/danieldiaz/Desktop/PickleFiles/docID2URL.pk","rb"))
        self.websiteresultsDict = None
        self.sorted_docs1 = None
        self.websiteresultsDict1 = None
        self.sorted_docs2 = None
        self.websiteresultsDict2 = None
        self.termIDExists1 = True
        self.termIDExists2 = True

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
        if (self.termid1 != ''):
            (self.docs, self.sorted_docs, self.websiteresultsDict1) = self.finddocs(self.termid1)
            self.websiteresultsDict = self.websiteresultsDict1
        #check result is not none
        else:
            self.websiteresultsDict = {}
            self.websiteresultsDict[0] = "No Results for that Query"

        return

    def calc2gram(self):
        self.termid1 = self.term_id_from_term(self.term1)
        self.termid2 = self.term_id_from_term(self.term2)
        #results for first word
        if (self.termid1 != ''):
            (self.docs1, self.sorted_docs1, self.websiteresultsDict1) = self.finddocs(self.termid1)
        else:
            self.websiteresultsDict1 = None
        #resultd for second word
        if (self.termid2 != ''):
            (self.docs2, self.sorted_docs2, self.websiteresultsDict1) = self.finddocs(self.termid2)
        else:
            self.websiteresultsDict2 = None
        #Zipper results
        (self.docs, self.sorted_docs, self.websiteresultsDict) = self.zipperresults(self.docs1,self.docs2)
        #will write results in websiteresultsDict
        return

    def constructResults(self):
        self.results['search_phrase'] = self.search_phrase
        self.results['term_id1'] = self.termid1
        self.results['websites'] = self.websiteresultsDict
        return self.results

    def term_id_from_term(self,term):
        try:
            term = term.lower()
            result = str(self.term2termid[term])
        except:
            result = None
            #result = "term not found"
        return result

    def finddocs(self,termid):
        docs = self.term2tfidf[int(termid)]
        #print(docs)
        sorted_docs = sorted(docs.items(), key=operator.itemgetter(1), reverse=True)
        #print("Sorted Docs")
            #print(sorted_docs)

            #firstpage = self.docid2url[firstdoc]
        websiteresultsDict = {}

        count = 0
        for tuple in sorted_docs:
            if (count < self.maxResults):
                websiteresultsDict[count] = self.docid2url[tuple[0]]
            else:
                break
            count += 1

        return docs, sorted_docs, websiteresultsDict

    def zipperresults(self,x,y):
        #base case
        #if both none
        if (x is None and y is None):
            self.websiteresultsDict = {}
            self.websiteresultsDict[0] = "No Results for that Query"
            return
        #if x is none
        if (x is None):
            self.websiteresultsDict = self.websiteresultsDict2
            return
        #if y is none
        if (y is None):
            self.websiteresultsDict = self.websiteresultsDict1
            return

        #zipper results
        zipperDict = {} #siteid, score
        count = 0
        for k,v in x.items():
            #k is doc id
            #v is score
            ######ONLY CARE ABOUT TOP 10 RESULTS
            if(count < self.maxResults):
                #check if doc id in other doc
                try:
                    yscore = y[int(k)]
                except:
                    yscore = 0
                zipperDict[k] = (yscore + v)/2
            else:
                break
            count += 1

        #reorder doc
        sorted_docs = sorted(zipperDict.items(), key=operator.itemgetter(1), reverse=True)

        count = 0
        websiteresultsDict = {}
        for tuple in sorted_docs:
            if (count < self.maxResults):
                websiteresultsDict[count] = self.docid2url[tuple[0]]
            else:
                break
            count += 1

        return zipperDict, sorted_docs, websiteresultsDict

