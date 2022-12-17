import json
from helperfuncs import emoji

class Lexicon:

    def __init__(self, file):

        self.path = file
        self.shouldDump = False
        self.len = 0
        self.words = {}

    def loadFromStorage(self):
        with open(self.path, 'r') as f:
            data = json.load(f)
            self.words = data["words"]
            self.len = data["len"]

        print(emoji("✔"), " Loaded",self.len,"words in lexicon")

    def addWord(self, word):
        if(word in self.words): return self.words[word]

        self.words[word] = self.len
        # print(word, self.words[word])
        self.len += 1
        self.shouldDump = True
        return self.len - 1

    def getWordID(self, word):
        return self.words[word]

    def dump(self):
        if(self.shouldDump):
            with open(self.path, "w") as outfile:
                json.dump({ "words": self.words, "len": self.len }, outfile)
