# Word Autocomplete System with AVL Tree

This project is a challenge proposed in the Algorithms and Data Structures 2 discipline at UFRN. The goal is to create a word completion system using an AVL tree.

## Description

The system loads a corpus (set of texts) and extracts all unique words, inserting them into an AVL tree. A function is implemented to receive a prefix (initial part of a word) and return a list of possible complete words found in the tree.

The performance of the AVL tree is compared with reference data structures such as a List and a Binary Tree. A minimal front end is implemented using Streamlit.

## Phases

1. Corpus Preprocessing: Text is converted to lowercase, punctuation and special characters are removed, text is split into words, and stop words are removed.

2. Construction of AVL Tree: All unique words from the corpus are inserted into the AVL tree.

3. Autocomplete: A function is implemented to traverse the AVL tree and return words that begin with a given prefix.

4. Performance Analysis: The performance of the AVL tree is compared with a List and a Binary Tree.

## Students

This project was carried out by Erich Brendell Araújo Medeiros and Mateus Rodrigues da Silva.

## Explanatory Video

An explanatory video about the solution and the main results can be found [[here](https://www.loom.com/share/d1f7453139d64e62af01ab28ac758f11?sid=92b91ad4-2933-40d1-8360-c9179d8f3336)https://www.loom.com/share/d1f7453139d64e62af01ab28ac758f11?sid=92b91ad4-2933-40d1-8360-c9179d8f3336](video_link).
