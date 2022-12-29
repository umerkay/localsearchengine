import json
from helperfuncs import emoji

class InvIndex:

    def __init__(self, path):
        self.wordIDs = {}
        self.path = path
        #{
        #    "wordID": [[docID, count], [docID, count]],
        #    "wordID": [[docID, count], [docID, count]]
        # }

    def generateFromFwdInd(self, FwdIndex):
        for docID in range(len(FwdIndex.docs)):
            self.appendDoc(FwdIndex.docs[docID], len(FwdIndex.docTable) - len(FwdIndex.docs) + docID)
        # for doc in FwdIndex.docs:
        #     self.appendDoc(doc)
    
    def appendDoc(self, doc, docID):
        for wordID in doc:
            # if(wordID == "wordCount"): continue
            #if this word is already indexed for this word, continue :)
            # if(docID in self.wordIDs[wordID]): continue
            #pls fix this
            wordID = str(wordID)
            #document ID, word count of wordid in docid, first occurence index of wordid in docid
            tuple = [doc[wordID][0], doc[wordID][1]]
            if(wordID in self.wordIDs):
                self.wordIDs[wordID][docID] = tuple
            else:
                self.wordIDs[wordID] = {}
                self.wordIDs[wordID][docID] = tuple

    def loadFromStorage(self):
        with open(self.path, 'r') as f:
            self.wordIDs = json.load(f)

        print(emoji("✔"), " Loaded",len(self.wordIDs),"words in inverted index")

    def dump(self):
        with open(self.path, "w") as outfile:
            json.dump(self.wordIDs, outfile)
        print("Inverted Index saved")

invInd = InvIndex("outputs/invIndex.json")