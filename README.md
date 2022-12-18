# Local Search Engine in Python

## About this Submission

This is a very basic readme file for the purposes of fulfilling the basic deliverable of the project. This readme will be updated as work is done on the project

Currently the indexing works, but is not fully optimized.

## Initial Testing

8840 articles with 28657 unique words were cleaned and indexed in 62.4 seconds (Ryzen 5,  4500U, plugged in) in "newsmax.json"
An average one word query takes 20ms to 30ms to execute, including ranking. This is not optimized at the time of this submission.

I am using stemming and lemmatization alternately in testing. The current code runs stemming, lemmatization is commented.

## Testing the Indexing

in ```main.py```
change the fileToIndex variable to change the dataset

```
fileToIndex = "data/________.json"

if __name__ == '__main__':
    genIndices(fileToIndex)
```

after generating the indices, you can simply load them in memory in the next run
```
if __name__ == '__main__':
    loadIndices()
```

Run main.py file.

## Lexicon and DocTable
The lexicon is a key value dictionary mapping each word to an assigned wordID
The DocTable simply stores the unique article ids in an ordered list, the index of the id is the DocID for internal code use. DocTable entries will be used to access document in original json data after querying

## Forward Index
The forward index stores a list of documents, each document is a dictionary with key value pairs.
Each key is a wordID that stores an array of positions of that word in the document.

```
[
    { "wordID": [a, b, c, d], "wordID": [a, b, c, d] }, "wordID": [a, b, c, d] } docID = 0
    { "wordID": [a, b, c, d], "wordID": [a, b, c, d] }, "wordID": [a, b, c, d] } docID = 1
]
```

Index of the document object is the docID.

## Inverted Index
The inverted index stores a dictionary of wordIDs. Each wordID stores an array of arrays in the following format

```
{
    "wordID": [[docID, wordCount], [docID, wordCount], [docID, wordCount]],
    "wordID": [[docID, wordCount], [docID, wordCount], [docID, wordCount]]
}
```

# Query
Query code works but that is not part of the submission.

# Sample Data
root/data folder holds sample data that has been tested against the current code.

## In-progress Improvements

Indexing uses .json and python dictionaries in storage and memory respectively.
I might convert code base to use numpy arrays and matrices for this matter to optimize both storage and memory usage. Numpy matrices/arrays will also improve ranking of results in querying
Most of the code base will remain the same, i will just add a container class to handle partial loading and unloading of data later on.
The lexicon generation requires further cleaning to cleanly process links or other words joined with punctuation
