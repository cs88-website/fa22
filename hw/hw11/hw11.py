
###################################
## Iterator/Generator Questions ##
###################################

def naturals(initial=1, step=1):
    i = initial
    while True:
        yield i
        i += step

# Q1
class IteratorRestart:
    """
    >>> iterator = IteratorRestart(2, 7)
    >>> for num in iterator:
    ...     print(num)
    2
    3
    4
    5
    6
    7
    >>> for num in iterator:
    ...     print(num)
    2
    3
    4
    5
    6
    7
    """
    def __init__(self, start, end):
        "*** YOUR CODE HERE ***"

    def __next__(self):
        "*** YOUR CODE HERE ***"

    def __iter__(self):
        "*** YOUR CODE HERE ***"


# Q2
def hailstone(n):
    """
    >>> for num in hailstone(10):
    ...     print(num)
    ...
    10
    5
    16
    8
    4
    2
    1
    """
    "*** YOUR CODE HERE ***"


# Q3
def generate_perms(lst):
    """
    Generates the permutations of lst one by one.
    >>> perms = generate_perms([1, 2, 3])
    >>> hasattr(perms, '__next__')
    True
    >>> p = list(perms)
    >>> p.sort()
    >>> p
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    """
    "*** YOUR CODE HERE ***"

