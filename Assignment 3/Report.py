import pickle


if __name__ == '__main__':
    file_count = pickle.load(open("Pickle Files/docID2URL.pk", 'rb'))
    print(file_count)
    terms = pickle.load(open("Pickle Files/docID2URL.pk", "rb"))
    print(len(terms))

