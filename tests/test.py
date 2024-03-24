import nltk
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.probability import FreqDist

nltk.download('punkt')

text = """Welcome to the Programming Knowledge! Lets start with our first tutorial on NLTK. NLTK is a leading platform for building Python programs to work with human language data. It provides easy-to-use interfaces to over 50 corpora and lexical resources such as WordNet, along with a suite of text processing libraries for classification, tokenization, stemming, tagging, parsing, and semantic reasoning, wrappers for industrial-strength NLP libraries, and an active discussion forum. Thanks for joining us. Have a great time learning with us."""

tokens = word_tokenize(text)
fd = FreqDist(tokens)

print(tokens) # Tokenizing words
print("\n")
print(sent_tokenize(text)) # Tokenizing sentences
# print(fd) # Frequency Distribution of words
# print(fd.most_common(5)) # Most common words
# fd.plot(30, cumulative=False) # Plotting the frequency distribution of words
# plt.show()