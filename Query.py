from helperfuncs import get_wordnet_pos, stemmer, lemmatizer, stop_words
from nltk.tokenize import word_tokenize
import string
import math

class Query:

    def __init__(self, fwdInd, invInd, lex, queryText):
        self.fwdInd = fwdInd
        self.invInd = invInd
        self.lex = lex
        self.queryText = queryText
        self.results = []

    def getResults(self):
        stringTxt = self.queryText.translate(str.maketrans('', '', string.punctuation))
        words = word_tokenize(stringTxt)

        # for i in range(len(words)):
        word_lower = words[0].lower()
        if word_lower not in stop_words:
            word_stem = stemmer.stem(word_lower)
            self.wordID = str(self.lex.getWordID(word_stem))
            (self.invInd.wordIDs)
            docsFound = self.invInd.wordIDs[self.wordID]

        self.results = docsFound
        print(len(self.results), "results found for query '", self.queryText, "'")
        return self

    def rankResults(self):
        for docEntry in self.results:
            docID = docEntry[0]
            count = docEntry[1]

            tf = (count) / (self.fwdInd.docs[docID]["wordCount"])
            idf = math.log(1 + (len(self.fwdInd.docs) / len(self.invInd.wordIDs[self.wordID])))
            # print(tf, idf, tf * idf)
            docEntry[0] = self.fwdInd.docTable[docID]
            docEntry[1] = tf * idf
        #should sort while looping to improve performance
        self.results.sort(key = lambda docEntry: docEntry[1], reverse = True)
        return self.results

    def setQueryText(self, text):
        self.queryText = text
