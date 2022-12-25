import json
from nltk.tokenize import word_tokenize, WordPunctTokenizer
from helperfuncs import get_wordnet_pos, stemmer, lemmatizer, stop_words, trackTime
import nltk
import string
from helperfuncs import emoji
from timeit import default_timer as timer
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import numpy
import os

tokenizer = WordPunctTokenizer()

# def processDoc(doc):
#     docFwdInd = {}
#     words = tokenizer.tokenize(doc["content"])
#     for i in range(len(words)):
#         word_lower = words[i].lower()
#         if word_lower.isalpha() and word_lower not in stop_words:
#             word_stem = stemmer.stem(word_lower)
#             id = str(lex.addWord(word_stem))

#             if(id in docFwdInd):
#                 docFwdInd[id].append(i)
#             else:
#                 docFwdInd[id] = [i]
    
#     return docFwdInd

def processDoc1(doc):
    words = tokenizer.tokenize(doc["content"])
    words2 = []
    # words2 = [doc["id"]]
    for i in range(len(words)):
        word_lower = words[i].lower()
        if word_lower.isalpha() and word_lower not in stop_words:
            words2.append(stemmer.stem(word_lower))
    
    return words2

def processDoc2(doc, lexiconObj):
    docFwdInd = {}
    for i in range(len(doc)):
            id = str(lexiconObj.getWordID(doc[i]))

            if(id in docFwdInd):
                docFwdInd[id].append(i)
            else:
                docFwdInd[id] = [i]
    
    return docFwdInd 

class FwdIndex:

    def __init__(self, file):
        self.docs = list()
        self.path = file
        self.shouldDump = False
        self.docTable = list()
        # [{
        #     "wordID": [pos1, pos2, ..., posn]
        # },{
        #     "wordID": [pos1, pos2, ..., posn]
        # }]

    def loadFromStorage(self):
        with open(self.path, 'r') as f:
            self.docs = json.load(f)

        with open("outputs/docTable.json", "r") as infile:
            self.docTable = json.load(infile)

        print(emoji("✔"), " Loaded",len(self.docs),"docs in forward index")

    def generateFromDir(self, lexiconObj, dir):
        for file in os.listdir(dir):
            self.generateFromFile(self, lexiconObj, os.path.join(dir, file))

    def generateFromFile(self, lexiconObj, file):
    
        with open(file, 'r') as f:
            data = json.load(f)

            with ProcessPoolExecutor() as executor:
                data = list(executor.map(processDoc1, data))

            lexWords = numpy.unique([token for doc in data for token in doc])
            for word in lexWords:
                lexiconObj.addWord(word)
        
            self.docs += [processDoc2(doc, lexiconObj) for doc in data]

            return len(data)

            # with ThreadPoolExecutor() as executor:
            #     self.docs = list(executor.map(processDoc, data))


    def addDoc(self, doc):
        self.docs.append(doc)
        self.shouldDump = True
        return len(self.docs) - 1

    def dump(self):
        # if(self.shouldDump == False): return
        with open(self.path, "w") as outfile:
            json.dump(self.docs, outfile)

        with open("outputs/docTable.json", "w") as outfile:
            json.dump(self.docTable, outfile)


fwdInd = FwdIndex("outputs/fwdIndex.json")