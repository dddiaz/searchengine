__author__ = 'Viral_Shah'


import pickle
import json
import os

import Logger
import Utilities
import Scoring

from collections import defaultdict
from nltk.corpus import stopwords

# initialize necessary dictionaries

class Indexer:
    def __init__(self):
        self.term2termID = defaultdict(str)
        self.term2DocIDFreq = defaultdict(dict)
        self.term2TFIDF = defaultdict(dict)
        self.docID2URL = defaultdict(dict)
        self.file_path = "/Users/Viral_Shah/Downloads/FileDump/"
        self.picklePath = "Pickle Files/"
        self.corpus_count = 0

    def index(self):
        self.loadPickle()
        for file in os.listdir(self.file_path)[self.corpus_count:]:
            if file == ".DS_Store":
                continue
            print(self.corpus_count)
            self.corpus_count += 1

            file_path = os.path.join(self.file_path, file)
            docID, text, title, url = self.parse_JSON(file_path)

            title_frequency = Utilities.frequency_counter(Utilities.parser(title))
            text_frequency = Utilities.frequency_counter(Utilities.parser(text))

            self.parse_corpus(docID, title_frequency, True)
            self.parse_corpus(docID, text_frequency)
            self.docID2URL[docID] = url

            # Logger.print_log(docID, file_path, text, text_frequency, title, title_frequency)
            # Logger.print_dicts(self.term2termID, self.term2DocIDFreq, self.term2TFIDF, self.corpus_count)
            self.sanitize()
        print("index complete")
        self.score_data()
        print("scoring complete")
        self.dump_pickle()
        print("done")

    def sanitize(self):
        for stopword in stopwords.words("english"):
            if stopword in self.term2termID.keys():
                self.term2termID.__delitem__(stopword)

    def loadPickle(self):
        try:
            pickle.load(self.term2TFIDF, open(self.picklePath + "term2TFIDF.pk", 'rb'))
            pickle.load(self.term2termID, open(self.picklePath + "term2termID.pk", 'rb'))
            pickle.load(self.term2DocIDFreq, open(self.picklePath + "term_freq.pk", 'rb'))
            pickle.load(self.corpus_count, open(self.picklePath + "file_count.pk", 'rb'))
            pickle.load(self.docID2URL, open(self.picklePath + "docID2URL.pk", 'rb'))
        except:
            pass

    def dump_pickle(self):
        pickle.dump(self.term2TFIDF, open(self.picklePath + "term2TFIDF.pk", 'wb'))
        pickle.dump(self.term2termID, open(self.picklePath + "term2termID.pk", 'wb'))
        pickle.dump(self.term2DocIDFreq, open(self.picklePath + "term_freq.pk", 'wb'))
        pickle.dump(self.corpus_count, open(self.picklePath + "file_count.pk", 'wb'))
        pickle.dump(self.docID2URL, open(self.picklePath + "docID2URL.pk", 'wb'))

    def parse_JSON(self, file_path):
        jsonData = json.load(open(file_path))
        docID = jsonData.get("id")
        title = jsonData.get("title")
        text = jsonData.get("text")
        url = jsonData.get("_id")
        return docID, text, title, url

    def mapTerm2TermID(self, term):
        if term not in self.term2termID.keys():
            self.term2termID[term] = len(self.term2termID)
        term_id = self.term2termID[term]
        return term_id

    def parse_corpus(self, docID, corpusFrequency, boost=False):
        for term in corpusFrequency.keys():
            term_id = self.mapTerm2TermID(term)
            if boost:
                if term_id in self.term2DocIDFreq.keys():
                    if docID in self.term2DocIDFreq[term_id].keys():
                        self.term2DocIDFreq[term_id][docID][0] += corpusFrequency[term]
                self.term2DocIDFreq[term_id][docID] = [corpusFrequency[term], 0]
            else:
                if term_id in self.term2DocIDFreq.keys():
                    if docID in self.term2DocIDFreq[term_id].keys():
                        self.term2DocIDFreq[term_id][docID][1] += corpusFrequency[term]
                self.term2DocIDFreq[term_id][docID] = [0, corpusFrequency[term]]

    def score_data(self):
        for term, doc_freq in self.term2DocIDFreq.items():
            for doc, freq in doc_freq.items():
                titleTF = Scoring.calculate_TF(int(freq[0]))
                textTF = Scoring.calculate_TF(int(freq[1]))
                idf = Scoring.calculate_IDF(self.corpus_count, len(doc_freq))
                TFIDF = Scoring.calculate_overall_score(titleTF, "title") * idf + Scoring.calculate_overall_score(textTF, "text") * idf
                self.term2TFIDF[term][doc] = TFIDF
        #print("TERM2TFIDF SCORE: ", self.term2TFIDF)


if __name__ == '__main__':
    n = Indexer()
    n.index()
