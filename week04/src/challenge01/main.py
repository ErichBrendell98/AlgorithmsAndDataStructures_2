import pytest
from bst import *

def findClosestValue(tree, target):
    """
    Finds the value in a binary search tree that is closest to the given target value.

    This function begins the search for the closest value from the root of the binary search tree.
    It works by recursively (or sequentialy) exploring the tree, narrowing down the search based on the target value
    and the current node's value. The closest value is constantly updated throughout the search process.

    Parameters:
    tree (BinarySearchTree): The binary search tree object in which to find the closest value.
                             It is expected to have a 'root' attribute that points to the root node of the tree.
    target (int): The target value for which the closest value in the binary search tree is sought.

    Returns:
    int: The value in the binary search tree that is closest to the target value.
    """

    return _findClosestValueInBstHelper(tree.root, target, float("inf"))

def _findClosestValueInBstHelper(node, target, closest):
    """
    Helper function for finding the value in a Binary Search Tree (BST) that is closest to a target value.

    This function uses a recursive approach to traverse the BST. At each node, it checks if the absolute difference 
    between the target value and the current node's value is less than the absolute difference between the target value 
    and the current closest value. If it is, it updates the closest value. Then, depending on whether the target value 
    is less than or greater than the current node's value, it makes a recursive call to the left or right child of the 
    current node, respectively.

    Args:
    - node (Node): The current node in the BST.
    - target (float): The target value.
    - closest (float): The current closest value to the target.

    Returns:
    - float: The value in the BST that is closest to the target value.
    """
    if node is None:
        return closest
    if abs(target - closest) > abs(target - node.value):
        closest = node.value
    if target < node.value:
        return _findClosestValueInBstHelper(node.left_child, target, closest)
    elif target > node.value:
        return _findClosestValueInBstHelper(node.right_child, target, closest)
    else:
        return closest



@pytest.fixture(scope="session")
def data():

    array = [[10, 5, 15, 13, 22, 14, 2, 5, 1],
             [100,5,502,204,55000,1001,4500,203,205,207,
              206,208,2,15,5,22,57,60,1,3,-51,1,1,1,1,1,-403]
             ]
    return array

def test_1(data):
    bst = BST()
    for value in data[0]:
        bst.add(value)
    assert findClosestValue(bst, 12) == 13

def test_2(data):
    bst = BST()
    for value in data[1]:
        bst.add(value)
    assert findClosestValue(bst, 100) == 100

def test_3(data):
    bst = BST()
    for value in data[1]:
        bst.add(value)
    assert findClosestValue(bst, 208) == 208

def test_4(data):
    bst = BST()
    for value in data[1]:
        bst.add(value)
    assert findClosestValue(bst, 4500) == 4500

def test_5(data):
    bst = BST()
    for value in data[1]:
        bst.add(value)
    assert findClosestValue(bst, 4501) == 4500

def test_6(data):
    bst = BST()
    for value in data[1]:
        bst.add(value)
    assert findClosestValue(bst, -70) == -51

def test_7(data):
    bst = BST()
    for value in data[1]:
        bst.add(value)
    assert findClosestValue(bst, 2000) == 1001

def test_8(data):
    bst = BST()
    for value in data[1]:
        bst.add(value)
    assert findClosestValue(bst, 6) == 5

def test_9(data):
    bst = BST()
    for value in data[1]:
        bst.add(value)
    assert findClosestValue(bst, 30000) == 55000

def test_10(data):
    bst = BST()
    for value in data[1]:
        bst.add(value)
    assert findClosestValue(bst, -1) == 1

def test_11(data):
    bst = BST()
    for value in data[1]:
        bst.add(value)
    assert findClosestValue(bst, 29751) == 55000

def test_12(data):
    bst = BST()
    for value in data[1]:
        bst.add(value)
    assert findClosestValue(bst, 29749) == 4500