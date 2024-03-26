import os
import time
import streamlit as st
from avl import AVLTree, BST
from corpus_preprocessing import corpus_preprocessing, download_file, remove_gutenberg_header_footer


def search_bst(tree, word, output):
    """
    Recursively searches for words in the BST that start with a given prefix.

    Args:
        tree (BST): The tree to start the search from.
        word (str): The prefix to search for in the BST.
        output (list): The list to append found words to.

    Returns:
        list: The list of words that start with the given prefix.
    """
    _search_bst_node(tree.root, word, output)
    return output

def _search_bst_node(node, word, output):
    if node is None:
        return
    if node.value.startswith(word):
        output.append(node.value)
    _search_bst_node(node.left_child, word, output)
    _search_bst_node(node.right_child, word, output)


def insert_into_list(words):
    """
    Inserts words into a list.

    Args:
        words (list): The words to insert into the list.

    Returns:
        list: The list with the inserted words.
    """
    word_list = []
    for word in words:
        word_list.append(word)
    return word_list


def insert_into_bst(words):
    """
    Inserts words into a Binary Search Tree (BST).

    Args:
        words (list): The words to insert into the BST.

    Returns:
        BST: The BST with the inserted words.
    """
    bst = BST()
    for word in words:
        bst.add(word)
    return bst


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

    # Create an AVL tree, a list and a BST
    bst = BST()
    word_list = []
    avl_tree = AVLTree()

    # Measure the time to insert words into the AVL tree, list, and BST
    start_time = time.time()
    for word in set(text_preprocessed):
        avl_tree.add(word)
    avl_insertion_time = time.time() - start_time

    start_time = time.time()
    word_list = insert_into_list(set(text_preprocessed))
    list_insertion_time = time.time() - start_time

    start_time = time.time()
    bst = insert_into_bst(set(text_preprocessed))
    bst_insertion_time = time.time() - start_time

    # Print the insertion times
    print(f"AVL tree insertion time: {avl_insertion_time}")
    print(f"List insertion time: {list_insertion_time}")
    print(f"BST insertion time: {bst_insertion_time}")

    # Measure the time to search for a prefix in the AVL tree, list, and BST
    prefix = "wha"
    # prefix = input("Enter the prefix you are looking for: ")
    start_time = time.time()
    search_bst(avl_tree, prefix, [])
    avl_search_time = time.time() - start_time

    start_time = time.time()
    [word for word in word_list if word.startswith(prefix)]
    list_search_time = time.time() - start_time

    start_time = time.time()
    search_bst(bst, prefix, [])
    bst_search_time = time.time() - start_time

    # Print the search times
    print(f"AVL tree search time: {avl_search_time}")
    print(f"List search time: {list_search_time}")
    print(f"BST search time: {bst_search_time}")

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