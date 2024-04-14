# README

## Solution Description

This repository contains an implementation of a function that finds the closest value to a target value in a Binary Search Tree (BST). The `findClosestValue` function takes a BST and a target value as input and returns the value in the BST that is closest to the target value.

The function uses a recursive approach to traverse the BST. At each node, it checks whether the absolute difference between the target value and the current node value is less than the absolute difference between the target value and the current closest value. If so, it updates the closest value. Then, depending on whether the target value is less than or greater than the value of the current node, it makes a recursive call to the left or right child of the current node, respectively.

## Instructions for Running the Solution

1. Clone the repository to your local machine.
2. Navigate to the repository directory in the terminal.
3. Run the command `pytest test_closest_value.py` to run the code.

## Algorithm Complexity

The time complexity of the algorithm is O(log(n)) in the average case, where n is the number of nodes in the BST. This occurs because at each step of the iteration, the algorithm discards half of the nodes in the BST. In the worst case, when the BST degenerates into a linked list, the time complexity is O(n).

The space complexity of the algorithm is O(1), as the `findClosestValue` function is iterative and does not use recursion. Therefore, the depth of the function call stack is not a factor in space complexity.

## Repository Organization and Structure

- `bst.py`: This file contains the definition of the `BST` and `Node` class.
- `closest_value.py`: This file contains the implementation of the `findClosestValue` function.
- `test_closest_value.py`: This file contains the unit tests for the `findClosestValue` function.
