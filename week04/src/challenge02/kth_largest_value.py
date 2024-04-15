from bst import BST


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

    # List to store nodes in reverse order
    nodes = []

    # Helper function to traverse the tree
    def reverse_in_order_traversal(node):
        if node is None or len(nodes) >= k:
            return
        reverse_in_order_traversal(node.right_child)
        if len(nodes) < k:
            nodes.append(node.value)
        reverse_in_order_traversal(node.left_child)

    # Start crossing
    reverse_in_order_traversal(tree.root)

    # Return the kth largest value
    return nodes[-1] if len(nodes) == k else -1