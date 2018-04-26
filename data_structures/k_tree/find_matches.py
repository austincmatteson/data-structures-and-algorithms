def find_matches(tree, val):
    """FInd all matching values in tree."""
    matches = []

    def _match(node):
        """Check for match."""
        nonlocal matches, val
        if node.val == val:
            matches.append(node)

    tree.pre_order(_match)
    return matches
