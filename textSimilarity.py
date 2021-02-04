import numpy as np

def __init__(self):
    self.s1 = ''
    self.s2 = ''
    self.s3 = ''
    self.stopwords = ''

def readInput(self,filename):
    try:
        with open(filename, 'r') as f:
            self.s1 = f.readline()
            self.s2 = f.readline()
            self.s3 = f.readline()
    except IOError:
        print("Error while reading the input file {}".format(filename))

    return self.s1,self.s2,self.s3

def getStopWords(self,filename):
    try:
        with open(filename, 'r') as f:
            self.stopwords = f.readlines()
            self.stopwords = [word.strip() for word in self.stopwords]
    except IOError:
        print("Error while reading the stopwords file {}".format(filename))

    return self.stopwords

def countWordFrequency(self, words):
    freq = {}
    for w in words:
        if w in freq:
            freq[w] = freq[w]+1
        else:
            freq[w] = 1
    return len(freq)

def getCosineSimilarity(a,b):
    dotProd = np.dot(a,b)
    n_a = np.linalg.norm(a)
    n_b = np.linalg.norm(b)
    return dotProd/(n_a*n_b)



