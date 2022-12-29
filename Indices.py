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
import threading

tokenizer = WordPunctTokenizer()

def genIndices(fileToIndex, hasloaded = False, lex = None):

    if(not hasloaded):
        lex = Lexicon("outputs/lexicon.json")

    print("Working on it...")
    print("Generating Forward Indices...")
    start = timer()

    # fwdInd.generateFromFile(lex, "data/newyorkpost.json")
    # fwdInd.generateFromFile(lex, fileToIndex)
    for file in os.listdir(fileToIndex):
        start2 = timer()

        docs = fwdInd.generateFromFile(lex, os.path.join(fileToIndex, file))
        
        elapsed2 = timer() - start2
        print(emoji("🕗"), file, "(" + str(docs) + ")", "took ", (str(round(elapsed2 * 1000)) + "ms") if elapsed2 < 1 else (str(round(elapsed2, 2)) + "s"))
    
    elapsed = timer() - start
    print(emoji("🕗"), "FwdInd took ", (str(round(elapsed * 1000)) + "ms") if elapsed < 1 else (str(round(elapsed, 2)) + "s"))
    
    start = timer()

    invInd.generateFromFwdInd(fwdInd)

    elapsed = timer() - start
    print(emoji("🕗"), "Inv Index took ", (str(round(elapsed * 1000)) + "ms") if elapsed < 1 else (str(round(elapsed, 2)) + "s"))

    # start = timer()
    def dumps():
        invInd.dump()
        fwdInd.dump(False)
        lex.dump()

    #can do this in thread
    t1 = threading.Thread(target=dumps)
 
    # starting thread 1
    t1.start()

    # elapsed = timer() - start
    # print(emoji("🕗"), "Dumping took ", (str(round(elapsed * 1000)) + "ms") if elapsed < 1 else (str(round(elapsed, 2)) + "s"))
    print(emoji("🚛"), "Dumping in background...")

def loadIndices():
    lex = Lexicon("outputs/lexicon.json")

    start = timer()

    lex.loadFromStorage()
    fwdInd.loadDocTableOnly()
    invInd.loadFromStorage()

    elapsed = timer() - start
    # print(emoji("🕗"), "Loading took ", (str(round(elapsed * 1000)) + "ms") if elapsed < 1 else (str(round(elapsed, 2)) + "s"))


    # start = timer()

    # # print(Query(fwdInd, invInd, lex, "rift last").getResults().rankResults())
    # # print(Query(fwdInd, invInd, lex, "last rift").getResults().rankResults())
    # print(Query(fwdInd, invInd, lex, "president").getResults().rankResults())
    # # print(Query(fwdInd, invInd, lex, "last").getResults().rankResults())

    # elapsed = timer() - start
    # print(emoji("🕗"), "Query took ", (str(round(elapsed * 1000)) + "ms") if elapsed < 1 else (str(round(elapsed, 2)) + "s"))
    return lex, fwdInd, invInd
   