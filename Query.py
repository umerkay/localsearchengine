from helperfuncs import get_wordnet_pos, stemmer, lemmatizer, stop_words
from nltk.tokenize import word_tokenize
import string
import math
from helperfuncs import emoji

class Query:

    def __init__(self, fwdInd, invInd, lex, queryText):
        self.fwdInd = fwdInd
        self.invInd = invInd
        self.lex = lex
        self.queryText = queryText
        self.results = []
        self.wordIDs = []

    def getResults(self):
        stringTxt = self.queryText.translate(str.maketrans('', '', string.punctuation))
        words = word_tokenize(stringTxt)

        for word in words:
            word_lower = word.lower()
            if word_lower not in stop_words:
                word_stem = stemmer.stem(word_lower)
                wordID = str(self.lex.getWordID(word_stem))
                # (self.invInd.wordIDs)
                self.results.append(self.invInd.wordIDs[wordID])
                self.wordIDs.append(wordID)

        # print(emoji("🚀"), len(self.results), "results found for query '" + self.queryText + "'")
        return self

    def rankResults(self):
        rankedResults = {}
        for i, wordResults in enumerate(self.results):
            for docEntry in wordResults:
                docID = docEntry[0]
                count = docEntry[1]

                tf = (count) / (self.fwdInd.docs[docID]["wordCount"])
                idf = math.log(1 + (len(self.fwdInd.docs) / len(self.invInd.wordIDs[self.wordIDs[i]])))
                 
                if(docID in rankedResults):
                    rankedResults[docID] += tf * idf
                else:
                    rankedResults[docID] = tf * idf
                # docEntry[0] = self.fwdInd.docTable[docID]
                docEntry[1] = tf * idf
                
        #should sort while looping to improve performance
        # self.results.sort(key = lambda docEntry: docEntry[1], reverse = True)
        # print(self.results)


        listed = rankedResults.items()
        self.results = sorted(listed, key = lambda docEntry: docEntry[1], reverse = True)
        #list of tuples
        print(emoji("🚀"), len(self.results), "results found for query '" + self.queryText + "'")
        # return self.results
        return (self.results[0], self.results[1], self.results[2])

    def setQueryText(self, text):
        self.queryText = text
