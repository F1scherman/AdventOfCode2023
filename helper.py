def extract_int(string):
    """This extracts an integer from a string. Breaks if multiple valid integers exist"""
    return int(''.join(filter(lambda a: a.isdigit(), string)))
