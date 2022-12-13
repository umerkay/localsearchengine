from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from helperfuncs import get_wordnet_pos
import nltk

stop_words = set(stopwords.words("english"))

example_string = """
running Muad'Dib learned rapidly because his first training was in how to learn. And the first lesson of all was the basic trust that he could learn. It's shocking to find how many people do not believe they can learn, and how many more believe learning to be difficult."""

words = word_tokenize(example_string)

filtered_list = [word for word in words if word.casefold() not in stop_words]
tagged = nltk.pos_tag(filtered_list)

print(words)
print(filtered_list)
print(tagged)

lemmatizer = WordNetLemmatizer()
# print(lemmatizer.lemmatize("plurals"))
lemmatized_words = [lemmatizer.lemmatize(word[0], get_wordnet_pos(word[1])) for word in tagged]
print(lemmatized_words)