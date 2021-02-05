import math
import string

stopwords = ''

def readInput(filename):
    try:
        with open(filename, 'r') as f:
            s1 = f.readline()
            s2 = f.readline()
            s3 = f.readline()
    except IOError:
        print("Error while reading the input file {}".format(filename))

    return s1,s2,s3

def getStopWords(filename):
    try:
        with open(filename, 'r') as f:
            stopwords = f.readlines()
            stopwords = [word.strip() for word in stopwords]
    except IOError:
        print("Error while reading the stopwords file {}".format(filename))

    return stopwords

def removeStopwords(text,stpwords):
    return ' '.join([w for w in text.split() if w not in stpwords])

def getWords(text):
    translation = str.maketrans(string.punctuation+string.ascii_uppercase," "*len(string.punctuation)+string.ascii_lowercase)
    text = text.translate(translation)
    lst = text.split()
    return lst

def countWordFrequency(words):
    freq = {}
    for w in words:
        if w in freq:
            freq[w] = freq[w]+1
        else:
            freq[w] = 1
    return freq

def dotProduct(a,b):
    total = 0.0
    for key in a:
        if key in b:
            total += (a[key]*b[key])
    return total

def similarity(a,b):
    num = dotProduct(a,b)
    denom = math.sqrt(dotProduct(a,a)*dotProduct(b,b))
    res = num/denom
    return res



