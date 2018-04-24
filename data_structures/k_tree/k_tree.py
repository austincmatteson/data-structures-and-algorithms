from q import Q


class KTree:
    """K-ary tree."""
    class Node:
        """Node for K-ary tree."""
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
        """Instatiate k-ary tree."""
        self.root = None

    def __repr__(self):
        """Represent root."""
        return '<K-ary Root {}>'.format(self.root.val)

    def __str__(self):
        """Root value."""
        return self.root.val

    def pre_order(self, operation):
        """Pre order traversal."""
        def _walk(node=None):
            """Traverse."""
            if node is None:
                return

            operation(node)

            for children in node.children:
                _walk(children)

        _walk(self.root)

    def post_order(self, operation):
        """Post order traversal."""
        def _walk(node=None):
            """Traverse."""
            if node is None:
                return
            for children in node.children:
                _walk(children)

            operation(node)

        _walk(self.root)

    def breadth_first_traversal(self, operation):
        """Breadth first traversal."""
        q = Q()
        temp_root = self.root
        q.enqueue(temp_root)
        while temp_root:
            for children in temp_root.children:
                q.enqueue(children)
            operation(temp_root)
            q.dequeue()
            if q.front is None:
                break
            temp_root = q.front.val

    def insert(self, val, parent=None):
        """Insert at selected parent."""
        def _find_parent(current):
            if current.val == parent:
                current.children.append(self.Node(val))
        node = self.Node(val)

        if self.root is None:
            self.root = node
            return node
        elif parent:
            self.breadth_first_traversal(_find_parent)
        else:
            raise ValueError('Please specify a parent value.')
