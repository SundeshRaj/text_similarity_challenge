import numpy as np
from flask import Flask, request, jsonify, render_template
from textSimilarity import *

app = Flask(__name__)
fSimilarity = ''
sSimilarity = ''
tSimilarity = ''
result = ''
inpFileName = 'data/input.txt'
stpWordsFileName = 'data/input.txt'

@app.route('/')
def homePage():
    global fSimilarity
    global sSimilarity
    global tSimilarity
    s1,s2,s3 = readInput(filename=inpFileName)
    stpWords = getStopWords(filename=stpWordsFileName)
    s1 = removeStopwords(s1, stpWords)
    s2 = removeStopwords(s2, stpWords)
    s3 = removeStopwords(s3, stpWords)

    s1Words = getWords(s1)
    s2Words = getWords(s2)
    s3Words = getWords(s3)

    s1CountFreq = countWordFrequency(s1Words)
    s2CountFreq = countWordFrequency(s2Words)
    s3CountFreq = countWordFrequency(s3Words)

    fSimilarity = "{:.6f}".format(similarity(s1CountFreq,s2CountFreq))
    sSimilarity = "{:.6f}".format(similarity(s2CountFreq,s3CountFreq))
    tSimilarity = "{:.6f}".format(similarity(s1CountFreq,s3CountFreq))

    return render_template('index.html', firstSimilarity=fSimilarity, secondSimilarity=sSimilarity, thirdSimilarity=tSimilarity)

@app.route('/getSimilarity', methods=['POST'])
def getSimilarity():
    inputStrings = [str(x) for x in request.form.values()]
    s1 = inputStrings[0]
    s2 = inputStrings[1]

    stpWords = getStopWords(filename=stpWordsFileName)

    s1 = removeStopwords(s1, stpWords)
    s2 = removeStopwords(s2, stpWords)

    s1Words = getWords(s1)
    s2Words = getWords(s2)

    s1CountFreq = countWordFrequency(s1Words)
    s2CountFreq = countWordFrequency(s2Words)

    fSim = "{:.6f}".format(similarity(s1CountFreq, s2CountFreq))

    result = 'The similarity between s1 and s2 is {}'.format(fSim)

    return render_template('index.html', firstSimilarity=fSimilarity, secondSimilarity=sSimilarity, thirdSimilarity=tSimilarity, result=result)

if __name__ == "__main__":
    app.run(debug=True)