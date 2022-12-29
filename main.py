from Indices import loadIndices, genIndices

# fileToIndex = "data/369news.json"
# fileToIndex = "data/newsmax.json"
dirToIndex = "data"

#reset all previous indexing
if __name__ == '__main__':
    genIndices(dirToIndex)
    
#append to previous indexing
if __name__ == '__main__':
    lex, fwdInd, invInd = loadIndices()
    # genIndices(fileToIndex)
    genIndices(dirToIndex, True, lex)