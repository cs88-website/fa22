def fib(n):
    """
    >>> fib(5)
    5
    """
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

def iter_fib(n):
    """
    >>> iter_fib(5)
    5
    """
    (n_1, n_2) = (0, 1)
    for i in range(0, n):
        # This computes n_1+n_2 before updating n_1
        (n_1, n_2) = (n_2, n_1 + n_2)
    return n_1

def count_change(value, coins):
    """Returns the number of ways to make change for amount.

    >>> denominations = [50, 25, 10, 5, 1]
    >>> count_change(7, denominations)
    2
    >>> count_change(100, denominations)
    292
    >>> denominations = [16, 8, 4, 2, 1]
    >>> count_change(7, denominations)
    6
    >>> count_change(10, denominations)
    14
    >>> count_change(20, denominations)
    60
    """
    if value < 0 or len(coins) == 0:
        return 0
    elif value == 0:
        return 1
    using_coin = count_change(value - coins[0], coins)
    not_using_coin = count_change(value, coins[1:])
    return using_coin + not_using_coin


import random

def random_list():
    return random.sample(range(0, 101), 20)

def split(x, s):
    return [i for i in s if i <= x], [i for i in s if i > x]

def quicksort(lst):
    """
    Sort a sequence - split it by the first element,
    sort both parts and put them back together.
    """
    if not lst:
        return []
    else:
        pivot = lst[0]
        smaller, bigger = split(pivot, lst[1:])
        return quicksort(smaller) + [pivot] + quicksort(bigger)


######### Example that's NOT functional,
### but conveys the idea of trees.

def is_file(thing):
    pass

def process_directory(directory):
    """
    This function does not do anything! It is a conceptual idea for tree recursion.
    """
    for item in directory:
        if is_file(item):
            process_file(item)
        else:
            processDirectory(item)
