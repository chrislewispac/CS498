import random 
import os
import string
import sys
import re

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
delimiterRegex = re.compile("[\\t,;.:?!\\-@\\[\\](){}_*/ ]")

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
    processedLinesArray = []
    d = dict()

    # read lines and filter by delimiters & stopWordsList
    for line in sys.stdin:
        cleaned = list(filter(None, delimiterRegex.split(line.lower().strip('\n').strip())))
        filtered = [x for x in cleaned if x not in stopWordsList]
        processedLinesArray.append(filtered)

    # iterate over the indices and select the corresponding line from the input txt
    for i in indexes:
    # take each word from the list & check if that word already exists in the dictionary 
        for word in processedLinesArray[i]:
            # if it already exists increment the count by 1
            if word in d:
                d[word] += 1
            # else insert into dictionary with count of 1
            else:
                d[word] = 1

    # add first 20 of sorted list to ret
    index = 0
    for x in sorted(d.items(), key=lambda x: (-x[1], x[0])):
        if index <=19:
            ret.append(x[0])
            index += 1
        else:
            break

                  
    for word in ret:
        print word

process(sys.argv[1])
