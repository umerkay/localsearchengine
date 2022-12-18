from Query import Query
from Lexicon import Lexicon
from FwdIndex import FwdIndex
from InvIndex import InvIndex
from timeit import default_timer as timer
from helperfuncs import emoji
from threading import Thread

global lex, fwdInd, invInd
lex = Lexicon("outputs/lexicon.json")
fwdInd = FwdIndex("outputs/fwdIndex.json")
invInd = InvIndex("outputs/invIndex.json")

def genIndices(fileToIndex):
    start = timer()
    print("Working on it...")

    fwdInd.generateFromFile(lex, fileToIndex)
    invInd.generateFromFwdInd(fwdInd)

    elapsed = timer() - start
    print(emoji("🕗"), "Generating took ", (str(round(elapsed * 1000)) + "ms") if elapsed < 1 else (str(round(elapsed, 2)) + "s"))

    start = timer()
    #can do this in thread
    invInd.dump()
    fwdInd.dump()
    lex.dump()

    elapsed = timer() - start
    print(emoji("🕗"), "Dumping took ", (str(round(elapsed * 1000)) + "ms") if elapsed < 1 else (str(round(elapsed, 2)) + "s"))


def loadIndices():
    start = timer()

    # thread = Thread(target=lex.loadFromStorage)
    # thread2 = Thread(target=fwdInd.loadFromStorage)
    # thread3 = Thread(target=invInd.loadFromStorage)

    # thread.start()
    # thread2.start()
    # thread3.start()

    # thread.join()
    # thread2.join()
    # thread3.join()

    lex.loadFromStorage()
    fwdInd.loadFromStorage()
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

   