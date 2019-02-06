import random 
import os
import string
import sys

stopWordsList = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours",
            "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its",
            "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that",
            "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having",
            "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
            "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
            "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
            "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
            "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
            "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

delimiters = " \t,;.?!-:@[](){}_*/"

def getIndexes(seed):
    random.seed(seed)
    n = 10000
    number_of_lines = 50000
    ret = []
    for i in range(0,n):
        ret.append(random.randint(0, 50000-1))
    return ret

def process(userID):
    indexes = getIndexes(userID)
    ret = []

    # TODO
    
    # 1) Divide each sentence into a list of words using delimiters provided in the “delimiters” 
    # variable; Make all the tokens lowercase (including special characters) and remove any 
    # tailing and leading spaces.

    # 2) One possible approach to deal with special (non-English) characters is to use decode() 
    # and encode(). For more information see:

    # 3) Ignore all common words provided in the “stopWordsList” variable.

    # 4) Keep track of word frequencies. To make the application more interesting, you have to 
    # process only the titles with certain indexes. These indexes are accessible using the 
    # “getIndexes” method, which returns an Integer List with 0-based indexes to the input file. 
    # It is possible to have an index appear several times. In this case, just process the 
    # index multiple times.

    # 5) Sort the words by frequency in a descending order. If two words have the same number count, 
    # use the lexigraphy. i.e. the following is sorted: {(Orange, 3), (Apple, 2), (Banana, 2)}

    # 6) Print out the top 20 items from the sorted list. (already implemented below)
                    
    for word in ret:
        print word

process(sys.argv[1])
