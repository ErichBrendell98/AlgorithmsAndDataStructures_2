from bst import BST


class Counter:
    def __init__(self):
        self.count = 0
        self.value = None


def findKthLargestValue(tree, k):
    """
    Finds the kth largest integer in a Binary Search Tree (BST).

    The function traverses the BST in an in-order manner to collect the node values in a sorted list.
    It then returns the kth largest value from this list. The BST is assumed to contain only integer values.
    In case of duplicate integers, they are treated as distinct values.
    The kth largest integer is determined in the context of these distinct values.

    Parameters:
    tree (BST): the Binary Search Tree (BST).
    k (int): A positive integer representing the kth position.

    Returns:
    int: The kth largest integer present in the BST.
    """
    counter = Counter()
    reverse_in_order_traversal(tree.root, k, counter)
    return counter.value


def reverse_in_order_traversal(node, k, counter):
    """
    Performs a reverse in-order traversal (right, root, left) on a Binary Search Tree (BST).

    The function traverses the BST in a reverse in-order manner to collect the node values in a descending ordered list.
    It then increments a counter each time a node is visited. When the counter is equal to k, the node value is stored.
    The BST is assumed to contain only integer values.
    In case of duplicate integers, they are treated as distinct values.
    The kth largest integer is determined in the context of these distinct values.

    Parameters:
    node: the current node in the BST.
    k (int): A positive integer representing the kth position.
    counter (Counter): A counter object that keeps track of the number of nodes visited and the kth largest value.

    Returns:
    Anything. The kth largest value is stored in the counter object.
    """
    if node is None or counter.count >= k:
        return
    reverse_in_order_traversal(node.right_child, k, counter)
    if counter.count < k:
        counter.count += 1
        counter.value = node.value
        reverse_in_order_traversal(node.left_child, k, counter)