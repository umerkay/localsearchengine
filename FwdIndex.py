import json
from nltk.tokenize import word_tokenize
from helperfuncs import get_wordnet_pos, stemmer, lemmatizer, stop_words
import nltk
import string
from helperfuncs import emoji

class FwdIndex:

    def __init__(self, file):
        self.docs = list()
        self.path = file
        self.shouldDump = False
        self.docTable = list()

    def loadFromStorage(self):
        with open(self.path, 'r') as f:
            self.docs = json.load(f)

        with open("outputs/docTable.json", "r") as infile:
            self.docTable = json.load(infile)

        print(emoji("✔"), " Loaded",len(self.docs),"docs in forward index")

    def generateFromFiles(self, lexiconObj, file):
        with open(file, 'r') as f:
            data = json.load(f)
            for doc in data:
                stringTxt = doc["content"].translate(str.maketrans('', '', string.punctuation))
                self.docTable.append(doc["id"])
                docFwdInd = {}

                words = word_tokenize(stringTxt)
                docFwdInd["wordCount"] = len(words)
                # tagged = nltk.pos_tag(words)

                for i in range(len(words)):
                    word_lower = words[i].lower()
                    if word_lower not in stop_words:
                        word_stem = stemmer.stem(word_lower)
                        # word_stem = lemmatizer.lemmatize(word_lower, get_wordnet_pos(tagged[i][1]))
                        id = str(lexiconObj.addWord(word_stem))

                        if(id in docFwdInd):
                            docFwdInd[id].append(i)
                        else:
                            docFwdInd[id] = [i]

                self.addDoc(docFwdInd)

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
        if(self.shouldDump == False): return
        with open(self.path, "w") as outfile:
            json.dump(self.docs, outfile)

        with open("outputs/docTable.json", "w") as outfile:
            json.dump(self.docTable, outfile)
