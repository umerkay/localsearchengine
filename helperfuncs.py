from nltk.corpus import wordnet
from nltk.corpus import stopwords
from nltk.stem import snowball
from nltk.stem import WordNetLemmatizer
import emoji as emojiLib
from timeit import default_timer as timer

stemmer = snowball.SnowballStemmer('english')
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))

def trackTime(name, f, args):
    start = timer()
    data = f(args)
    elapsed = timer() - start
    print(emoji("🕗"), name, "took", (str(round(elapsed * 1000)) + "ms") if elapsed < 1 else (str(round(elapsed, 2)) + "s"))
    return data

def emoji(e):
    return emojiLib.emojize(emojiLib.demojize(e))

def get_wordnet_pos(treebank_tag):

    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        # As default pos in lemmatization is Noun
        return wordnet.NOUN