from Query import Query
from Lexicon import Lexicon
from FwdIndex import FwdIndex
from InvIndex import InvIndex

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
    lex.loadFromStorage()
    fwdInd.loadFromStorage()
    invInd.loadFromStorage()

    #queryDocIDs("tyranny", lex, invInd, fwdInd)
    print(Query(fwdInd, invInd, lex, "TikTok").getResults().rankResults())