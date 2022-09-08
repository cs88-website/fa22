# List Comprehensions
courses = ['CS 88', 'DATA 8', 'POLSCI 2', 'MATH 54']

# Make a list from a for loop in one line!
numbers = [x * 2 for x in range(10) ]
# print(numbers)

# print() returns None
# [print(c) for c in courses]

# Copy a list!
courses2 = [c for c in courses]


# Functions are named, and we can assign new names

my_print = print

# my_print('Hello')

def greet(name):
    return 'Hello, ' + name + '!'

say_hello = greet

say_hello('CS88')

# Generalizing patterns using arguments

from math import pi, sqrt
from operator import mul

# Functions as arguments

def square(n):
    return n * n

def sum_numbers(n):
    """Sum the first N natural numbers.

    >>> sum_numbers(5)
    15
    """
    total = 0
    for i in range(n + 1):
        total += i
    return total

def sum_squared(n):
    """Sum the first N cubes of natural numbers.

    >>> sum_cubes(5)
    0
    """
    total = 0
    for i in range(n + 1):
        total = total + square(i)
    return total

def sum_cubes(n):
    """Sum the first N cubes of natural numbers.

    >>> sum_cubes(5)
    225
    """
    total = 0
    for i in range(n + 1):
        total = total + pow(i, 3)
    return total

def identity(k):
    return k

def cube(k):
    return pow(k, 3)

def summation(n, term):
    """Sum the first N terms of a sequence.

    >>> summation(5, cube)
    225
    >>> summation(5, identity)
    15
    """
    total = 0
    for i in range(n + 1):
        total = total + term(i)
    return total

def sum_error(n, term):
    """Sum the first N terms of a sequence.

    >>> summation(5, cube)
    225
    >>> summation(5, identity)
    15
    """
    total = 0
    for i in range(n + 1):
        total = total + term
    return total


from operator import mul

def pi_term(k):
    return 8 / mul(k * 4 - 3, k * 4 - 1)

summation(10000, pi_term)

def pi_error(approx):
    return str((1 - summation(approx, pi_term) / pi) * 100) + '%'


def add_one(n):
    return n + 1

add_one(3)

def make_adder(n):
    def adder(x):
        return x + n
    return adder

add_1 = make_adder(1)
x = add_1(3)

add_4 = make_adder(4)
add_4(5)

def compose(f, g):
    def h(x):
      return f(g(x))
    return h

add_2 = make_adder(2)
add_3 = make_adder(3)
x = add_2(x)

add_5 = compose(add_2, add_3)
y = add_5(x)

z = compose(square, make_adder(2))(3)
