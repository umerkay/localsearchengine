import json
from helperfuncs import emoji

class InvIndex:

    def __init__(self, path):
        self.wordIDs = {}
        self.path = path

    def generateFromFwdInd(self, FwdIndex):
        for docID in range(len(FwdIndex.docs)):
            for wordID in FwdIndex.docs[docID]:
                if(wordID == "wordCount"): continue
                #pls fix this
                wordID = str(wordID)
                tuple = [docID, len(FwdIndex.docs[docID][wordID])]
                if(wordID in self.wordIDs):
                    self.wordIDs[wordID].append(tuple)
                else:
                    self.wordIDs[wordID] = [tuple]

    def loadFromStorage(self):
        with open(self.path, 'r') as f:
            self.wordIDs = json.load(f)

        print(emoji("✔"), " Loaded",len(self.wordIDs),"words in inverted index")

    def dump(self):
        with open(self.path, "w") as outfile:
            json.dump(self.wordIDs, outfile)
