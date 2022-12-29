from Indices import loadIndices, genIndices

# fileToIndex = "data/369news.json"
# fileToIndex = "data/newsmax.json"
fileToIndex = "data"

if __name__ == '__main__':
    lex, fwdInd, invInd = loadIndices()
    # genIndices(fileToIndex)
    # genIndices(fileToIndex, True, lex)