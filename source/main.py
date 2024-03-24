import os
from corpus_preprocessing import corpus_preprocessing, download_file, remove_gutenberg_header_footer

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