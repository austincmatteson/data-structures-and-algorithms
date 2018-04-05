from stack import Stack


def multi_bracket_validation(string):
    """Check for balanced brackets."""
    open_bracket = Stack()
    for item in string:
        if item in ('{', '[', '('):
            open_bracket.push(item)
        elif item in ('}', ']'):
            if chr(ord(item) - 2) != open_bracket.pop():
                return False
        elif item == ')':
            if chr(ord(item) - 1) != open_bracket.pop():
                return False
    if open_bracket._size == 0:
        return True
    return False
