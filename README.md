# Local Search Engine in Python
This project has been made as part of the coursework required for CS250 Data Structures & Algorithms. The project demonstrates text indexing and querying capabilities.

# Interface
## Home Page
A lot of work has been put into the design of the UI
![image](https://user-images.githubusercontent.com/20483712/210053035-1508eb8a-517f-43e4-9381-39d5026bc789.png)

## Multiword Search
Multiword and Single word query and ranking can be tested using the provided UI
![image](https://user-images.githubusercontent.com/20483712/210053056-14c09b0c-ef63-4e39-9798-fa62325fea99.png)
![image](https://user-images.githubusercontent.com/20483712/210053061-d0ce3370-3ea3-4550-9d0e-6aa665708e62.png)

## Pagenation
![image](https://user-images.githubusercontent.com/20483712/210053243-cd1572af-5549-4a27-9fcb-4c37d3a90182.png)

## Uploading new files
Following UI can be used to index more files of the same format
![image](https://user-images.githubusercontent.com/20483712/210053114-efca01ee-8065-40ca-86c3-9040810fbb27.png)

# Setup 👩‍🔬
## Run Application 🚀
Before running, please create an outputs folder in the project root.
```
outputs/
    lexicon.json
    invIndex.json
    fwdIndex.json
    docTable.json
```
Then, before running the flask server, please index files first to avoid errors. (See below for instructions on indexing)

To run the latest commit, run the following command in the project root.

```flask run```

You can now perform search queries.
You can also use the UI to add new documents into the index dynamically, no need to restart the server 🥳

## Current Testing
Around 125k articles can be indexed within 100s, with around 70k words in lexicon.
Queries and ranking on average take 20 to 30ms

## Initial Testing

8840 articles with 28657 unique words were cleaned and indexed in 62.4 seconds (Ryzen 5,  4500U, plugged in) in "newsmax.json"
An average one word query takes 20ms to 30ms to execute, including ranking. This is not optimized at the time of this submission.

I am using stemming and lemmatization alternately in testing. The current code runs stemming, lemmatization is commented.

## Run Indexer 📇

in ```main.py```
change the fileToIndex variable to change the dataset
It takes a directory and forms indexes for all files inside the directory

```
fileToIndex = "data/________"

if __name__ == '__main__':
    genIndices(fileToIndex)
```

after generating the indices, you can simply load them in memory in the next run
```
if __name__ == '__main__':
    loadIndices()
```

Run main.py file.

### The details below may not align with the latest commit, as more information has since been added. Refer to project presentation

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

# Sample Data
root/data folder holds sample data that has been tested against the current code.
