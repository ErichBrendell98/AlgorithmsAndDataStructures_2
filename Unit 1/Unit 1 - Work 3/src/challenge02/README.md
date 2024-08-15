# Kth Largest Value in a Binary Search Tree

This repository contains a Python implementation for finding the kth largest value in a Binary Search Tree (BST).

## Solution Description

The implemented solution uses a reverse in-order traversal (right, root, left) of the BST. The traversal stops as soon as the kth largest value is found, making the solution time and space efficient.

## How to run

1. Clone the repository to your local machine.
2. Navigate to the repository directory in the terminal.
3. Run the command `pytest test_kth_largest_value.py` to run the code.

## Algorithm Complexity

The time complexity of the algorithm is O(h + k) in the average case, where h is the height of the BST and k is the input parameter. This is because at each step of the traversal, the algorithm visits the next node in reverse order. In the worst case, when BST degenerates into a linked list, the time complexity is O(n).

The space complexity of the algorithm is O(h) because the `findKthLargestValue` function uses a recursive traversal, and therefore the depth of the function call stack is a factor in the space complexity. However, the function has been optimized to stop the traversal as soon as the kth largest value is found, which may result in less space usage in practice.

## Repository Organization and Structure

- `bst.py`: This file contains the definition of the `BST` and `Node` class.
- `kth_largest_value.py`: This file contains the implementation of the `findKthLargestValue`, `reverse_in_order_traversal` functions and `Counter` class.
- `test_kth_largest_value.py`: This file contains the unit tests for the `findKthLargestValue` function.
