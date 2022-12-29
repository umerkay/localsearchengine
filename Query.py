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
            word_stem = stemmer.stem(word_lower)
            wordID = str(self.lex.getWordID(word_stem))

            if wordID in self.invInd.wordIDs:
                # wordID = word_stem
                # if(wordID == '-1'):
                    # continue
                # (self.invInd.wordIDs)
                self.results.append(self.invInd.wordIDs[wordID])
                self.wordIDs.append(wordID)

        # print(emoji("🚀"), len(self.results), "results found for query '" + self.queryText + "'")
        return self

    def rankResults(self, pageStart, pageSize):
        rankedResults = {}
        for i, wordResults in enumerate(self.results):
            for docEntry in wordResults:
                docID = int(docEntry)
                count = wordResults[docEntry][0]
                firstOccurence = wordResults[docEntry][1]

                #tf = count / totalwords (0 < tf <= 1)
                #idf = totalDocs / noOfDocsWithWord  (1 + 1 < idf <= totalDocs)
                #ipx = totalWords / firstIndex (1 < px < totalwords)
                tf = (count) / (self.fwdInd.docTable[docID][1])
                idf = 1 + (len(self.fwdInd.docTable) / len(self.invInd.wordIDs[self.wordIDs[i]]))
                ipx = (self.fwdInd.docTable[docID][1]) / firstOccurence #inverse proximity

                # docID = self.fwdInd.docTable[docID][0]
                if(docID in rankedResults):
                    rankedResults[docID] += tf * math.log(idf * ipx)
                else:
                    rankedResults[docID] = tf * math.log(idf * ipx)
                #dont change the docentry obj pls it changes the invindex
                # docEntry[0] = self.fwdInd.docTable[docID]
                # docEntry[1] = tf * idf
                
        #should sort while looping to improve performance
        # self.results.sort(key = lambda docEntry: docEntry[1], reverse = True)
        # print(self.results)


        listed = rankedResults.items()
        self.results = sorted(listed, key = lambda docEntry: docEntry[1], reverse = True)
        #list of tuples
        # print(emoji("🚀"), len(self.results), "results found for query '" + self.queryText + "'")
        # return self.results
        start = pageStart * pageSize
        end = min(pageStart * pageSize + pageSize - 1, len(self.results) - 1)
        return (list(map((lambda el: {"Title":  self.fwdInd.docTable[el[0]][0], "Score": el[1]}), self.results[start:end+1])), len(self.results))

    def setQueryText(self, text):
        self.queryText = text
