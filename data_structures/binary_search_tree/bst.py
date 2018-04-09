class Node:
    """Node for bst."""
    def __init__(self, val):
        """Instantiate node."""
        self.val = val
        self.right = None
        self.left = None

    def __repr__(self):
        """Represent node."""
        return '<Node Val: {}'.format(self.val)

    def __str__(self):
        """Node value."""
        return self.val


class BST:
    """Binary search tree."""
    def __init__(self):
        """Instatiate bst."""
        self.root = None

    def __repr__(self):
        """Represent root."""
        return '<BST Root {}>'.format(self.root.val)

    def __str__(self):
        """Root value."""
        return self.root.val

    def in_order(self, operation):
        """In order traversal."""
        def _walk(node=None):
            """Traverse."""
            if node is None:
                return

            if node.left is not None:
                _walk(node.left)

            operation(node)

            if node.right is not None:
                _walk(node.right)

        _walk(self.root)

    def pre_order(self, operation):
        """Pre order traversal."""
        def _walk(node=None):
            """Traverse."""
            if node is None:
                return

            operation(node)

            if node.left is not None:
                _walk(node.left)

            if node.right is not None:
                _walk(node.right)

        _walk(self.root)

    def post_order(self, operation):
        """Post order traversal."""
        def _walk(node=None):
            """Traverse."""
            if node is None:
                return

            if node.left is not None:
                _walk(node.left)

            if node.right is not None:
                _walk(node.right)

            operation(node)

        _walk(self.root)

    def insert(self, val):
        """Add value as node to bst."""
        node = Node(val)
        current = self.root

        if self.root is None:
            self.root = node
            return node

        while current:
            if val >= current.val:
                if current.right is not None:
                    current = current.right
                else:
                    current.right = node
                    break

            elif val < current.val:
                if current.left is not None:
                    current = current.left
                else:
                    current.left = node
                    break

        return node
