from bst import BST, Node


def findClosestValue(tree, target):
    """
    Finds the value in a binary search tree that is closest to the given target value.

    This function starts searching for the closest value from the root of the binary search tree.
    It works by exploring the tree iteratively, restricting the search based on the target value
    and the value of the current node. The closest value is constantly updated during the search process.

    Parameters:
    tree (BinarySearchTree): The binary search tree object in which to find the closest value.
                             It is expected to have a 'root' attribute that points to the root node of the tree.
    target (int): The target value for which the closest value in the binary search tree is searched.

    Returns:
    int: The value in the binary search tree that is closest to the target value.
    """
    closest = float('inf')
    currentNode = tree.root
    while currentNode is not None:
        if abs(target - closest) > abs(target - currentNode.value):
            closest = currentNode.value
        if target < currentNode.value:
            currentNode = currentNode.left_child
        elif target > currentNode.value:
            currentNode = currentNode.right_child 
        else:
            break
    return closest