import os
import streamlit as st
from corpus_preprocessing import corpus_preprocessing, download_file, remove_gutenberg_header_footer
from avl import AVLTree


def search_bst(tree, word, output):
    """
    Recursively searches for words in the BST that start with a given prefix.

    Args:
        tree (AVLTree or AVLNode): The tree or node to start the search from.
        word (str): The prefix to search for in the BST.
        output (list): The list to append found words to.

    Returns:
        list: The list of words that start with the given prefix.
    """
    if isinstance(tree, AVLTree):
        node = tree.root
    else:
        node = tree

    if node is None:
        return output

    if node.value.startswith(word):
        output.append(node.value)

    output = search_bst(node.left_child, word, output)
    output = search_bst(node.right_child, word, output)

    return output


def main():
    """
    Main function to run the application. It downloads the book "Moby Dick", preprocesses the text,
    inserts all unique words into an AVL tree, and provides an autocomplete feature based on the user's input.

    Args:
        None

    Returns:
        None
    """
    # URL of the book "Moby Dick" on Project Gutenberg
    url = "https://www.gutenberg.org/files/2701/2701-0.txt"
    local_filename = "moby_dick.txt"
    if not os.path.exists(local_filename):
        download_file(url, local_filename)
    with open(local_filename, 'r', encoding='utf-8-sig') as f:
        text_without_preprocessing = f.read()
    text_without_preprocessing = remove_gutenberg_header_footer(text_without_preprocessing)
    text_preprocessed = corpus_preprocessing(text_without_preprocessing)

    # Create an AVL tree
    avl_tree = AVLTree()

    # Inserts all unique words from the corpus into the AVL tree
    for word in set(text_preprocessed):
        avl_tree.add(word)

    st.header("Autocomplete")
    st.write("The tool will autocomplete the user's input.")

    prefix = st.text_input("Enter the input: ")
    v = []
    if len(prefix) != 0:
        st.write(search_bst(avl_tree, prefix, v))


if __name__ == "__main__":
    main()