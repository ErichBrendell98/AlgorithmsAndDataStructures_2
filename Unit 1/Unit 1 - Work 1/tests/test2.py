import nltk
# nltk.download('stopwords')

text = """Welcome to the Programming Knowledge! Lets start with our first tutorial on NLTK. NLTK is a leading platform for building Python programs to work with human language data. It provides easy-to-use interfaces to over 50 corpora and lexical resources such as WordNet, along with a suite of text processing libraries for classification, tokenization, stemming, tagging, parsing, and semantic reasoning, wrappers for industrial-strength NLP libraries, and an active discussion forum. Thanks for joining us. Have a great time learning with us."""
demoWords = ["playing", "happiness", "going", "yes", "no", "I", "having", "had", "haved"]

from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
# print(stop_words)

from nltk.tokenize import word_tokenize
word_tokenize = word_tokenize(text)
# print(word_tokenize)

word_tokenize_withoutStopWords = []
for word in word_tokenize:
    if word not in stop_words:
        word_tokenize_withoutStopWords.append(word)

print("Stop words that have been removed:", set(word_tokenize) - set(word_tokenize_withoutStopWords))
print("\n")
print(word_tokenize)
print("\n")
print(word_tokenize_withoutStopWords)
