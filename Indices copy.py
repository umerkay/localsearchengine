from Query import Query
from FwdIndex import fwdInd
from InvIndex import invInd
from Lexicon import Lexicon
from timeit import default_timer as timer
from helperfuncs import emoji
from helperfuncs import stop_words, stemmer
from threading import Thread
import os
from nltk.tokenize import word_tokenize, WordPunctTokenizer
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import numpy
import json

tokenizer = WordPunctTokenizer()

def genIndices(fileToIndex):

    lex = Lexicon("outputs/lexicon.json")

    print("Working on it...")
    # print("Generating Forward Indices...")
    # start = timer()

    # # fwdInd.generateFromFile(lex, "data/newyorkpost.json")
    # # fwdInd.generateFromFile(lex, fileToIndex)
    # for file in os.listdir(fileToIndex):
    #     start2 = timer()

    #     docs = fwdInd.generateFromFile(lex, os.path.join(fileToIndex, file))
        
    #     elapsed2 = timer() - start2
    #     print(emoji("🕗"), file, "(" + str(docs) + ")", "took ", (str(round(elapsed2 * 1000)) + "ms") if elapsed2 < 1 else (str(round(elapsed2, 2)) + "s"))
    
    # elapsed = timer() - start
    # print(emoji("🕗"), "FwdInd took ", (str(round(elapsed * 1000)) + "ms") if elapsed < 1 else (str(round(elapsed, 2)) + "s"))
    
    start = timer()

    # invInd.generateFromFwdInd(fwdInd)
    for file in os.listdir(fileToIndex):
        QuickIndexing(os.path.join(fileToIndex, file))
    

    elapsed = timer() - start
    print(emoji("🕗"), "Inv Index took ", (str(round(elapsed * 1000)) + "ms") if elapsed < 1 else (str(round(elapsed, 2)) + "s"))

    start = timer()
    #can do this in thread
    invInd.dump()
    fwdInd.dump()
    lex.dump()

    elapsed = timer() - start
    print(emoji("🕗"), "Dumping took ", (str(round(elapsed * 1000)) + "ms") if elapsed < 1 else (str(round(elapsed, 2)) + "s"))

def _quickInvIndex(i, doc):
    words2 = [stemmer.stem(word.lower()) for word in tokenizer.tokenize(doc["content"]) if word.lower().isalpha() and word.lower() not in stop_words]

    lexicon, word_hits = numpy.unique(words2, return_counts=True)

    for (wordID, word_hit) in zip(lexicon, word_hits):
        if(wordID in invInd.wordIDs):
            invInd.wordIDs[wordID].append((i, int(word_hit)))
        else:
            invInd.wordIDs[wordID] = [(i, int(word_hit))]
    
    # return (lexicon, word_hits)
    # return (lexicon, word_hits, doc["id"])
    # for i in range(len(lexicon)):
        # docInvInd[lexicon[i]] = [indx, word_hits[i]]

def QuickIndexing(file):
    with open(file, 'r') as f:
        docs = json.load(f)

        for (i,doc) in enumerate(docs):
            _quickInvIndex(i, doc)

        print(len(docs))
        return len(docs)
        # with ProcessPoolExecutor() as executor:
        #     docs = list(executor.map(_quickInvIndex, docs))

        # for i in range(len(docs)):
        #     # (lexicon, word_hits, docID) = docs[i]
        #     (lexicon, word_hits) = docs[i]
        #     # fwdInd.docTable.append(docID)
        #     for j in range(len(lexicon)):
        #         wordID = lexicon[j]
        #         if(wordID in invInd.wordIDs):
        #             invInd.wordIDs[wordID].append((i, int(word_hits[j])))
        #         else:
        #             invInd.wordIDs[wordID] = [(i, int(word_hits[j]))]

def loadIndices():
    lex = Lexicon("outputs/lexicon.json")

    start = timer()

    # lex.loadFromStorage()
    # fwdInd.loadFromStorage()
    invInd.loadFromStorage()

    elapsed = timer() - start
    print(emoji("🕗"), "Loading took ", (str(round(elapsed * 1000)) + "ms") if elapsed < 1 else (str(round(elapsed, 2)) + "s"))


    # start = timer()

    # # print(Query(fwdInd, invInd, lex, "rift last").getResults().rankResults())
    # # print(Query(fwdInd, invInd, lex, "last rift").getResults().rankResults())
    # print(Query(fwdInd, invInd, lex, "president").getResults().rankResults())
    # # print(Query(fwdInd, invInd, lex, "last").getResults().rankResults())

    # elapsed = timer() - start
    # print(emoji("🕗"), "Query took ", (str(round(elapsed * 1000)) + "ms") if elapsed < 1 else (str(round(elapsed, 2)) + "s"))
    return lex, fwdInd, invInd
   