# Some handy imports, don't worry about these
# This file needs to be run locally on you machine,
# it displays graphical output.
### Docs: https://docs.python.org/3.8/library/turtle.html

# Run with python3 -i 10-Recursion.py

"""
General Recuesion Examples.

A syntax note:
print (f"N: {n}, Squared: {squared}")
f tells python to interpret {n} as an expression
this is the same as:
print("N: " + str(n) + ", Squared: " + str(squared))
...which is messier to read. :)
"""

from os import name

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

def iter_fact(n):
    result = 1:
    for i in range(1, n+1):
        result *= i
    return result

def simple_fact(n):
    return product(range(1, n + 1))

from functools import reduce
from operator import mul
def hof_fact(n):
    return reduce(mul, range(1, n + 1))

def sum_of_sqaures_print(n):
    print("Sum n: ", n)
    if n < 1:
        return 0
    # elif n < 0: # what if we wanted to handle negative numbers?
        # return sum_of_sqaures_print(n * -1)
        # return squared + sum_of_sqaures_print(n + 1)
    else:
        squared = n**2
        # print (f"N: {n}, Squared: {squared}")
        return squared + sum_of_sqaures_print(n - 1)

def sum_of_sqaures(n):
    if n < 1:
        return 0
    else:
        return n**2 + sum_of_sqaures(n - 1)

def countdown(n):
    if n == 0:
        print('Blastoff!')
    else:
        # What happens if we swap the order?
        print(n)
        countdown(n - 1)

# countdown(2)
    # countdown(1)
    #   countdown(0)
    #   print(1)
    # print(2)

# def countdown_print(n):
#     if n == 0:
#         print('Blastoff!')
#     else:
#         # What happens if we swap the order?
#         print(f'Before: {n}')
#         countdown(n - 1)
#         print(f'After: {n}')

def reverse(s):
    """
    >>> reverse('hello')
    'olleh'
    >>> reverse(reverse('hello'))
    'hello'
    """
    if not s:
        return ''
    return reverse(rest(s)) + first(s)

def reverse_2(s):
    """
    >>> reverse_2('hello')
    'olleh'
    >>> reverse_2(reverse_2('hello'))
    'hello'
    """
    if not s:
        return ''
    last = s[-1]
    all_but_last = s[0:-1]
    return last + reverse(all_but_last)

def first(s):
    """Return the first element in a sequence."""
    return s[0]

def rest(s):
    """Return all elements in a sequence after the first"""
    return s[1:]

def min_r(s):
    """Return minimum value in a sequence."""
    if len(s) == 1:
        return first(s)
    else:
        return min(first(s), min_r(rest(s)))

def palindrome(word):
  if len(word) == 1:
    return True
  elif word[0] == word[-1]:
    return palindrome(word[1:-1])
  return False

def reverse_for(s):
    """
    >>> reverse_for('hello')
    'olleh'
    """
    result = ''
    for letter in s:
        result = letter + result
        print(result)
    return result

def reverse_while(s):
    """
    >>> reverse_while('hello')
    'olleh'
    """
    result = ''
    while s:
        first = s[0]
        s = s[1:] # remove the first letter
        result = first + result
    return result


def reverse_print(s):
    """
    >>> reverse_recur('hello')
    'olleh'
    """
    if not s:
        return ''
    print('Pre-recursive-call:' , s[0], s[1:])
    result = reverse_print(s[1:]) + s[0]
    print(result)
    return result

def palindrome_iter(word):
    """"
    >>> palindrome_iter('racecar')
    True
    """
    while word:
        if word[0] != word[-1]:
            return False
        word = word[1:-1]
    return True
