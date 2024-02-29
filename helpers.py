def normalize_line_endings(s):
    """
    Normalize the line endings in a string to Unix-like (\n), without altering
    escape sequences within string literals.
    
    :param s: The string with potential mixed line endings (\r\n, \r, \n).
    :return: A string with normalized line endings (\n).
    """
    return s.replace('\r\n', '\n').replace('\r', '\n')

