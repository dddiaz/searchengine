__author__ = 'Viral_Shah'

def print_dicts(term2termID, term2DocIDFreq, term2TFIDF, corpus_count):
    print("===========================BEGIN===================================")
    print("TERM2TERMID: ", term2termID)
    print()
    print("TERM2DOCIDFREQ: ", term2DocIDFreq)
    print()
    print("TERM2TFIDF: ", term2TFIDF)
    print()
    print("CORPUSCOUNT: ", corpus_count)
    print("============================END==================================")

def print_log(docID, file_path, text, text_frequency, title, title_frequency):
    print()
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("FILE PATH: ", file_path)
    print()
    print("DOCID: ", docID)
    print()
    print("TITLE: ", title)
    print()
    print("TEXT: ", text)
    print()
    print("Title Frequency: ", title_frequency.items())
    print()
    print("Text Frequency: ", text_frequency.items())
    print()