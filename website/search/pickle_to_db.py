__author__ = 'danieldiaz'

import pickle

file_count = pickle.load( open( "/Users/danieldiaz/Desktop/PickleFiles/file_count.pk", "rb" ) )
count1 = 0
print(file_count)

term_freq = pickle.load( open( "/Users/danieldiaz/Desktop/PickleFiles/term_freq.pk", "rb" ) )
count2 = 0
for key, value in term_freq.items():
    print (key, value)
    count2 += 1
    if (count2 == 10):
        break



term_tfidf = pickle.load( open( "/Users/danieldiaz/Desktop/PickleFiles/term_tfidf.pk", "rb" ) )

count3 = 0
for key, value in term_freq.items():
    print (key, value)
    count3 += 1
    if (count3 == 5):
        break

# word hash : wordid -> word
# word_hash = pickle.load( open( "/Users/danieldiaz/Desktop/PickleFiles/word_hash.pk", "rb" ) )
#
# count4 = 0
# for key, value in term_freq.items():
#     print (key, value)
#     count4 += 1
#     if (count4 == 5):
#         break