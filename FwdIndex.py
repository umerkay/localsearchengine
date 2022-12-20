import json
from nltk.tokenize import word_tokenize, WordPunctTokenizer
from helperfuncs import get_wordnet_pos, stemmer, lemmatizer, stop_words
import nltk
import string
from helperfuncs import emoji

tokenizer = WordPunctTokenizer()

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

    def __processWord(self, docFwdInd, word_lower, i, lexiconObj):
        if word_lower.isalpha() and word_lower not in stop_words:
            word_stem = stemmer.stem(word_lower)
            # word_stem = lemmatizer.lemmatize(word_lower, get_wordnet_pos(tagged[i][1]))
            # word_stem = lemmatizer.lemmatize(word_lower)
            id = str(lexiconObj.addWord(word_stem))

            if(id in docFwdInd):
                docFwdInd[id].append(i)
            else:
                docFwdInd[id] = [i]

    def generateFromFiles(self, lexiconObj, files):
        for file in files:
            self.generateFromFile(self, lexiconObj, file)

    def generateFromFile(self, lexiconObj, file):
        _punct = str.maketrans('', '', string.punctuation)

        with open(file, 'r') as f:
            data = json.load(f)
            for doc in data:
                # stringTxt = doc["content"].translate(_punct)
                self.docTable.append(doc["id"])
                docFwdInd = {}

                # words = word_tokenize(doc["content"])
                # titlewords = word_tokenize(doc["title"])
                words = tokenizer.tokenize(doc["content"])

                docFwdInd["wordCount"] = len(words)
                
                #reduce function calls for optimization and fast running pls thx <3
                #title words have 0 position always, other positions start from 1....n
                # for word in titlewords:
                #     self.__processWord(docFwdInd, word, 0, lexiconObj)

                for i in range(len(words)):
                    word_lower = words[i].lower()
                    if word_lower.isalpha() and word_lower not in stop_words:
                        word_stem = stemmer.stem(word_lower)
                        id = str(lexiconObj.addWord(word_stem))

                        if(id in docFwdInd):
                            docFwdInd[id].append(i)
                        else:
                            docFwdInd[id] = [i]

                # self.addDoc(docFwdInd)
                
                self.docs.append(docFwdInd)

                # tagged = nltk.pos_tag(words)
                # words = word_tokenize(string)
                # filtered_list = set([word for word in words if word.casefold() not in stop_words])
                # tagged = nltk.pos_tag(filtered_list)
                # lemmatized_words = [lemmatizer.lemmatize(word[0], get_wordnet_pos(word[1])) for word in tagged]

                # #can optimize here
                # for word in lemmatized_words:
                #     lex1.addWord(word)  

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
