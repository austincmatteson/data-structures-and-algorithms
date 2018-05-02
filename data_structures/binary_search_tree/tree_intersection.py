def tree_intersection(tree1, tree2):
    """Return all matching values of two trees."""
    one, two, match = set(), set(), set()
    tree1.pre_order(one.add)
    tree2.pre_order(two.add)
    for each in one:
        if each in two:
            match.add(each.val)
    return match
