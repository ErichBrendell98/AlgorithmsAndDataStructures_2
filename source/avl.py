class Node:
    """
    Represents a node in a Binary Search Tree (BST).

    Each node has a value and two children: left_child and right_child.

    Attributes:
        value: The value stored in the node.
        left_child (Node or None): The left child of the node. Initializes to None when the node is created.
        right_child (Node or None): The right child of the node. Initializes to None when the node is created.
    """

    def __init__(self, value):
        """
        Initializes a node with a value and no children.

        Args:
            value: The value to be stored in the node.
        """
        self.value = value
        self.left_child = None
        self.right_child = None


class BST:
    """
    Represents a Binary Search Tree (BST).

    Attributes:
        root (Node or None): The root node of the tree. Initializes to None for an empty tree.
    """

    def __init__(self):
        """Initializes an empty BST."""
        self.root = None

    def add(self, value):
        """
        Inserts a new value into the BST.

        Args:
            value: The value to be added to the tree.

        If the tree is empty, the value becomes the root. Otherwise, the method uses
        a recursive helper function to find the appropriate position to maintain the BST property.
        """
        if self.root is None:
            self.root = Node(value)
        else:
            self._add_recursive(self.root, value)

    def _add_recursive(self, current_node, value):
        """
        Recursively finds the correct position and inserts a value into the BST.

        Args:
            current_node (Node): The node to start the search for the insert position from.
            value: The value to be added to the BST.

        The method determines if the new value should be placed to the left or right of
        the current node. If the target position is empty, the value is inserted.
        Otherwise, the function calls itself recursively with the respective child node.
        """
        if value <= current_node.value:
            if current_node.left_child is None:
                current_node.left_child = Node(value)
            else:
                self._add_recursive(current_node.left_child, value)
        else:
            if current_node.right_child is None:
                current_node.right_child = Node(value)
            else:
                self._add_recursive(current_node.right_child, value)

    def _contains(self, current_node, value):
        """
        Recursively checks if the BST contains the specified value starting from a given node.

        Args:
            current_node (Node): The node to start the search from.
            value: The value to search for in the BST.

        Returns:
            bool: True if the value exists in the subtree rooted at current_node, otherwise False.
        """
        if current_node is None:
            return False
        if current_node.value == value:
            return True
        if value < current_node.value:
            return self._contains(current_node.left_child, value)
        return self._contains(current_node.right_child, value)

    def contains(self, value):
        """
        Checks if the BST contains the specified value.

        Args:
            value: The value to search for in the BST.

        Returns:
            bool: True if the BST contains the value, otherwise False.
        """
        return self._contains(self.root, value)


class AVLNode(Node):
    """
    Represents a node in an AVL (Adelson-Velsky and Landis) tree,
    which is a self-balancing binary search tree.

    Attributes:
        height (int): The height of the subtree rooted at this node,
                      initializes to 1 when the node is created.
        imbalance (int): The imbalance factor of this node, calculated
                         as the difference between the heights of the left
                         and right subtrees. Initializes to 0.

    Inherits from:
        Node: Inherits attributes and methods from the Node class.
    """

    def __init__(self, value):
        """
        Initializes an AVLNode with a given value.

        Args:
            value: The value to be stored in this node.
        """
        super().__init__(value)
        self.height = 1
        self.imbalance = 0

    def calculate_height_and_imbalance(self):
        """
        Calculates the height and imbalance factor of this node based
        on the heights of its left and right children.

        This method assumes that the heights of the children nodes (if they exist)
        are up-to-date.
        """
        # Calculate the height of the left child subtree
        left_height = 0
        if self.left_child is not None:
            left_height = self.left_child.height

        # Calculate the height of the right child subtree
        right_height = 0
        if self.right_child is not None:
            right_height = self.right_child.height

        # Update the height of this node
        self.height = 1 + max(left_height, right_height)

        # Calculate and update the imbalance factor for this node
        self.imbalance = left_height - right_height


class AVLTree(BST):
    """
    Represents an AVL (Adelson-Velsky and Landis) tree, a self-balancing binary search tree.
    Inherits all attributes and methods from the BST class and overrides some to maintain the AVL balance property.

    Attributes:
        Inherits all attributes from the BST class.
    """

    def __init__(self):
        """
        Initializes an empty AVL Tree.
        """
        super().__init__()

    def add(self, value):
        """
        Overrides the add method in the BST class to handle AVL Tree balancing.
        """
        self.root = self._add_recursive(self.root, value)  # Note that self.root is updated here

    def _add_recursive(self, current_node, value):
        """
        Overrides the BST method to recursively find the correct position and insert a value into the AVL tree.
        This method also ensures the tree remains balanced by updating node heights and performing rotations as needed.

        Args:
            current_node (AVLNode or Node or None): The node from which to start the search for the insert position.
            value (Any): The value to be added to the AVL tree.

        Returns:
            AVLNode: The node that either gets inserted or the node that was already present at that position.

        Notes:
            1.  The method first checks if the current_node is an instance of the base class Node.
                If it is, the method casts it to AVLNode to ensure AVL properties are maintained. This is especially
                useful if the first node added to the tree is of type Node; this ensures subsequent nodes will be of
                type AVLNode.
            2.  The method also balances the tree by calling the _balance method if the imbalance factor
                of a node reaches 2 or -2 after an insert operation.
        """

        # If the current node is None, return a new AVLNode containing the value
        if current_node is None:
            return AVLNode(value)

        # Check if current_node is of the base class Node and cast it to AVLNode if necessary
        # This is necessary to not change the add() in the BST class.
        # When the first node is added, the type of the root is Node, so we need to cast it
        if isinstance(current_node, Node) and not isinstance(current_node, AVLNode):
            current_node = AVLNode(current_node.value)
            current_node.left_child = self.root.left_child
            current_node.right_child = self.root.right_child
            self.root = current_node

        # Determine whether the value should be inserted to the left or right subtree
        if value <= current_node.value:
            current_node.left_child = self._add_recursive(current_node.left_child, value)
        else:
            current_node.right_child = self._add_recursive(current_node.right_child, value)

        # Update the height and imbalance factor for the current node
        current_node.calculate_height_and_imbalance()

        # Check if tree balancing is needed and balance if necessary
        if abs(current_node.imbalance) == 2:
            return self._balance(current_node)

        return current_node

    def get_height(self):
        """
        Retrieves the height of the AVL Tree.

        Returns:
            int: The height of the tree rooted at self.root. Returns 0 if the tree is empty.
        """
        if self.root is None:
            return 0
        return self.root.height

    def _rotate_left(self, node):
        """
        Performs a left rotation on the given node and adjusts the height and imbalance attributes.

        A left rotation is used to balance an AVL Tree when the right subtree of a node
        becomes higher than the left subtree. The method updates the heights and imbalance
        factors for the rotated nodes.

        Args:
            node (AVLNode): The node to be rotated.

        Returns:
            AVLNode: The new root node of the rotated subtree (the pivot).
        """

        # Store the pivot (the root of the right subtree of 'node')
        pivot = node.right_child

        # Update the right child of 'node' to be the left child of the pivot
        node.right_child = pivot.left_child

        # Set the left child of the pivot to be the node
        pivot.left_child = node

        # Recalculate the height and imbalance factor for the rotated node
        node.calculate_height_and_imbalance()

        # Recalculate the height and imbalance factor for the pivot
        pivot.calculate_height_and_imbalance()

        # Return the pivot as the new root of this subtree
        return pivot

    def _rotate_right(self, node):
        """
        Performs a right rotation on the given node and adjusts the height and imbalance attributes.

        A right rotation is used to balance an AVL Tree when the left subtree of a node
        becomes higher than the right subtree. This method updates the heights and imbalance
        factors for the rotated nodes.

        Args:
            node (AVLNode): The node around which the rotation will be performed.

        Returns:
            AVLNode: The new root node of the rotated subtree (the pivot).
        """

        # Store the pivot (the root of the left subtree of 'node')
        pivot = node.left_child

        # Update the left child of 'node' to be the right child of the pivot
        node.left_child = pivot.right_child

        # Set the right child of the pivot to be the node
        pivot.right_child = node

        # Recalculate the height and imbalance factor for the rotated node
        node.calculate_height_and_imbalance()

        # Recalculate the height and imbalance factor for the pivot
        pivot.calculate_height_and_imbalance()

        # Return the pivot as the new root of this subtree
        return pivot

    def _balance(self, node):
        """
        Balances the subtree rooted at the given node by performing rotations as needed.

        If the imbalance factor of the given node is 2 or -2, rotations are performed
        to bring the subtree back into balance. This method also takes into account
        the imbalance factors of the child nodes to decide which type of rotation is needed
        (single or double).

        Args:
            node (AVLNode): The root node of the subtree that needs to be balanced.

        Returns:
            AVLNode: The new root node of the balanced subtree.

        Note:
            This method assumes that the height and imbalance factor of each node are up-to-date.
        """

        # Case 1: Left subtree is higher than right subtree
        if node.imbalance == 2:
            pivot = node.left_child
            # Single right rotation
            if pivot.imbalance == 1:
                return self._rotate_right(node)
            # Double rotation: Left-Right
            else:
                node.left_child = self._rotate_left(pivot)
                return self._rotate_right(node)
        # Case 2: Right subtree is higher than left subtree
        else:
            pivot = node.right_child
            # Single left rotation
            if pivot.imbalance == -1:
                return self._rotate_left(node)
            # Double rotation: Right-Left
            else:
                node.right_child = self._rotate_right(pivot)
                return self._rotate_left(node)
