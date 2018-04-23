class BST:
    """Binary search tree."""
    class Node:
        """Node for k-ary_tree."""
        def __init__(self, val):
            """Instantiate node."""
            self.val = val
            self.children = []

        def __repr__(self):
            """Represent node."""
            return '<Node Val: {}'.format(self.val)

        def __str__(self):
            """Node value."""
            return self.val

    def __init__(self):
        """Instatiate bst."""
        self.root = None

    def __repr__(self):
        """Represent root."""
        return '<BST Root {}>'.format(self.root.val)

    def __str__(self):
        """Root value."""
        return self.root.val
