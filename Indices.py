from Query import Query
from Lexicon import Lexicon
from FwdIndex import FwdIndex
from InvIndex import InvIndex
from timeit import default_timer as timer
from helperfuncs import emoji

global lex, fwdInd, invInd
lex = Lexicon("outputs/lexicon.json")
fwdInd = FwdIndex("outputs/fwdIndex.json")
invInd = InvIndex("outputs/invIndex.json")

def genIndices():
    fwdInd.generateFromFiles(lex, "data/newsmax.json")
    fwdInd.dump()
    lex.dump()

    invInd = InvIndex("outputs/invIndex.json")
    invInd.generateFromFwdInd(fwdInd)
    invInd.dump()

    #queryDocIDs("able", lex, invInd, fwdInd)
    # print(Query(fwdInd, invInd, lex, "able").getResults())
    # print(Query(fwdInd, invInd, lex, "tyranny").getResults().rankResults())

def loadIndices():
    start = timer()

    lex.loadFromStorage()
    fwdInd.loadFromStorage()
    invInd.loadFromStorage()

    elapsed = timer() - start
    print(emoji("🕗"), "Loading took ", (str(round(elapsed * 1000)) + "ms") if elapsed < 1 else (str(round(elapsed, 2)) + "s"))


    # start = timer()

    # print(Query(fwdInd, invInd, lex, "rift last").getResults().rankResults())
    # print(Query(fwdInd, invInd, lex, "last rift").getResults().rankResults())
    # print(Query(fwdInd, invInd, lex, "rift").getResults().rankResults())
    # print(Query(fwdInd, invInd, lex, "last").getResults().rankResults())

    # elapsed = timer() - start
    # print(emoji("🕗"), "Query took ", (str(round(elapsed * 1000)) + "ms") if elapsed < 1 else (str(round(elapsed, 2)) + "s"))

   