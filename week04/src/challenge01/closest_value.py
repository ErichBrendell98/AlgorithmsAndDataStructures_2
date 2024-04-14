from bst import BST, Node


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