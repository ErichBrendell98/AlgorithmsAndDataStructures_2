import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

def corpus_preprocessing(text):
    """
    Performs pre-processing of the provided corpus.

    This pre-processing includes converting the text to
    lowercase, the removal of punctuation and special characters, the division of text into words (tokenization) and the removal of stop words.

    Parameters:
    text (str): The text to be preprocessed.

    Returns:
    list: A list of tokens after preprocessing.
    """
    # Convert all text to lowercase
    text = text.lower()
    # Remove punctuation and special characters
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Splits text into words
    tokens = word_tokenize(text)
    # Remove stop words
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]

    print(tokens)

if __name__ == "__main__":
    text_without_preprocessing = """Welcome to the Programming Knowledge! Lets start with our first tutorial on NLTK. NLTK is a leading platform for building Python programs to work with human language data. It provides easy-to-use interfaces to over 50 corpora and lexical resources such as WordNet, along with a suite of text processing libraries for classification, tokenization, stemming, tagging, parsing, and semantic reasoning, wrappers for industrial-strength NLP libraries, and an active discussion forum. Thanks for joining us. Have a great time learning with us."""

    text_preprocessed = corpus_preprocessing(text_without_preprocessing)
    print(text_preprocessed)