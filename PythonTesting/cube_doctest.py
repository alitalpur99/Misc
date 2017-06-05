"""Function Testing using Doctest"""

def cube(n):
    """
    >>> cube(2)
    8
    >>> cube(5)
    125
    >>> cube(6)
    216
    >>> cube(7)
    343"""
    return n**3

if __name__ == "__main__": 
    import doctest
    doctest.testmod(verbose=True, optionflags=doctest.NORMALIZE_WHITESPACE)
    #doctest.testmod # For non-verbose output
