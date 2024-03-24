import os
import string

import nltk
import requests
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

    return tokens


def download_file(url, local_filename):
    """
    Downloads a file from the provided URL and saves it locally.

    Parameters:
    url (str): The URL of the file to download.
    local_filename (str): The name of the local file where the downloaded file should be saved.

    Returns:
    str: The local file path.
    """
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_filename


def remove_gutenberg_header_footer(text):
    """
    Removes the header and footer from Project Gutenberg text.
    The beginning of the book is marked "*** START OF THIS PROJECT GUTENBERG EBOOK"
    and the end of the book is marked by "*** END OF THIS PROJECT GUTENBERG EBOOK"

    Parameters:
    text (str): The text to remove the header and footer from.

    Returns:
    str: The text without the header and footer.
    """
    start_marker = "*** START OF THIS PROJECT GUTENBERG EBOOK"
    end_marker = "*** END OF THIS PROJECT GUTENBERG EBOOK"
    start_index = text.find(start_marker) + len(start_marker)
    end_index = text.find(end_marker)
    return text[start_index:end_index]


if __name__ == "__main__":
    # URL of the book "Moby Dick" on Project Gutenberg
    url = "https://www.gutenberg.org/files/2701/2701-0.txt"
    local_filename = "moby_dick.txt"
    if not os.path.exists(local_filename):
        download_file(url, local_filename)
    with open(local_filename, 'r', encoding='utf-8-sig') as f:
        text_without_preprocessing = f.read()
    text_without_preprocessing = remove_gutenberg_header_footer(text_without_preprocessing)
    text_preprocessed = corpus_preprocessing(text_without_preprocessing)
    print(text_preprocessed)