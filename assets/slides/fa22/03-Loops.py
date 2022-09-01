"""
This is a comment for the entire file!
Doctests can test pretty much anything in Python.
>>> 1 + 1
2
"""

def max(x, y):
    """Returns the larger value of arguments x and y
    >>> max(6, 0)
    6
    """
    return x if x > y else y


def countdown(num):
    print('Counting down!')
    while num > 0:
        print(num)
        num = num - 1
    print("Done!")
