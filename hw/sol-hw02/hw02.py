"""Homework 2."""

def fib(n):
    """Returns the nth Fibonacci number.

    >>> fib(0)
    0
    >>> fib(1)
    1
    >>> fib(2)
    1
    >>> fib(3)
    2
    >>> fib(4)
    3
    >>> fib(5)
    5
    >>> fib(6)
    8
    >>> fib(100)
    354224848179261915075
    """
    curr, next = 0, 1
    while n > 0:
        curr, next = next, curr + next
        n -= 1
    return curr


def nonzero(lst):
    """ Returns the first nonzero element of a list

    >>> nonzero([1, 2, 3])
    1
    >>> nonzero([0, 1, 2])
    1
    >>> nonzero([0, 0, 0, 0, 0, 0, 5, 0, 6])
    5
    """
    for i in lst:
        if i != 0:
            return i


def has_n(lst, n):
    """ Returns whether or not a list contains the value n.

    >>> has_n([1, 2, 2], 2)
    True
    >>> has_n([0, 1, 2], 3)
    False
    >>> has_n([], 5)
    False
    """
    for elem in lst:
        if elem == n:
            return True
    return False


def total_price(prices):
    """
    Finds the total price of all products in prices including a
    50% tax on products with a price greater than or equal to 20.
    >>> total_price([5, 20, 30, 7])
    87
    >>> total_price([8, 4, 3])
    15
    >>> total_price([10, 100, 4])
    164
    """
    return int(sum([x if x < 20 else 1.5*x for x in prices]))


def arange(start, end, step=1):
    """
    arange behaves just like np.arange(start, end, step).
    You only need to support positive values for step.

    >>> arange(1, 3)
    [1, 2]
    >>> arange(0, 25, 2)
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]
    >>> arange(999, 1231, 34)
    [999, 1033, 1067, 1101, 1135, 1169, 1203]

    """
    return [n for n in range(start, end, step)]


def reverse_iter_for(lst):
    """Returns the reverse of the given list.

    >>> reverse_iter_for([1, 2, 3, 4])
    [4, 3, 2, 1]
    """
    rev_lst = []
    for e in lst:
        rev_lst = [e] + rev_lst
    return rev_lst

def reverse_iter_while(lst):
    """Returns the reverse of the given list.

    >>> reverse_iter_while([1, 2, 3, 4])
    [4, 3, 2, 1]
    """
    rev_lst, i = [], 0
    while i < len(lst):
        rev_lst = [lst[i]] + rev_lst
        i += 1
    return rev_lst

