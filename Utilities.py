import collections
import itertools
import string
import os
import nltk
from nltk import bigrams
from nltk import trigrams

letters = string.ascii_letters
digits = string.digits
punctuations = string.punctuation

lettersdict = dict.fromkeys(letters, 0)
digitsdict = dict.fromkeys(digits, 0)
punctuationsdict = dict.fromkeys(punctuations, 0)

mainsequence = letters + digits + punctuations

bigram = list()
bigramtuple = list(itertools.product(mainsequence, mainsequence))
for item in bigramtuple:
    bigram.append(item[0] + item[1])

trigram = list()
trigramtuple = list(itertools.product(mainsequence, mainsequence, mainsequence))
for item in trigramtuple:
    trigram.append(item[0] + item[1] + item[2])

bigramdict = dict.fromkeys(bigram, 0)
trigramdict = dict.fromkeys(trigram, 0)

maindictionary = {**lettersdict, **digitsdict,
                  **punctuationsdict, **bigramdict, **trigramdict}


def pad(text):
    n = len(text) % 8
    # print(n)
    if n != 0:
        return text + (b'\x00' * (8 - n))
    else:
        return text


def remove_ws_equal(text):
    text = text.replace(" ", "")
    text = text.replace("=", "")
    return text


def top10000pass():
    count = 0

    with open("rockyou.txt") as fp:
        while count < 10000:
            count += 1
            line = fp.readline().strip()
            yield line

            if not line:
                break


def word2ngramdict(text):
    textunigrams = getunigramdict(text)
    textbigrams = getngram2dict(text)
    texttrigrams = getngram3dict(text)
    totalgrams = {**textunigrams, **textbigrams, **texttrigrams}
    textdictionary = maindictionary.copy()
    textdictionary.update(totalgrams)
    return textdictionary


def iterateoverfiles(directory):
    # iterate over files in
    # that directory
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isfile(f):
            yield f


def getngram2dict(text):
    text2gram = list()
    tokenized = [*text]
    bitokenstuplegen = bigrams(tokenized)
    bitokenstuple = list(bitokenstuplegen)
    for item in bitokenstuple:
        text2gram.append(item[0] + item[1])

    bigramsdict = {}
    for token in text2gram:
        if token not in bigramsdict:
            bigramsdict[token] = 1
        else:
            bigramsdict[token] += 1

    return bigramsdict


def getngram3dict(text):
    text2gram = list()
    tokenized = [*text]
    tritokenstuplegen = trigrams(tokenized)
    tritokenstuple = list(tritokenstuplegen)
    for item in tritokenstuple:
        text2gram.append(item[0] + item[1] + item[2])

    trigramsdict = {}
    for token in text2gram:
        if token not in trigramsdict:
            trigramsdict[token] = 1
        else:
            trigramsdict[token] += 1

    return trigramsdict


def getunigramdict(text):
    tokenized = [*text]

    unigramsdict = {}
    for token in tokenized:
        if token not in unigramsdict:
            unigramsdict[token] = 1
        else:
            unigramsdict[token] += 1

    return unigramsdict


text ='aaasdasfasdasdasfa'


