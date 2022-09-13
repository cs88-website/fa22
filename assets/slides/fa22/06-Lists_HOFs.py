from operator import add, mul, concat
from functools import reduce

def add_one(n):
    return n + 1

add_one(3)

def make_adder(n):
    def adder(x):
        return x + n
    return adder

add_1 = make_adder(1)
add_1(3)

add_4 = make_adder(4)
add_4(5)

def leq_maker(c):
    def leq(val):
        return val <= c
    return leq

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

# help(map)

def is_even(n):
    return n % 2 == 0

def is_uppercase(word):
    return word[0].capitalize() == word[0]

def shout(word):
    return word.upper()

def embiggen(item):
    "This uses some Python features we don't really cover, but can be fun."
    if type(a) == str:
        return shout(item)
    elif item.isdigit():
        return int(item) * 2
    else:
        return item

cal = 'The University of California at Berkeley'
copycats = 'The University of California Los Angeles'
jc = 'Leland Stanford Junior University'

words = cal.split()
# words
# # ['The', 'University', 'of', 'Califonria', 'at', 'Berkeley']
# numbers = range(10)
# [ n * n for n in numbers ]
# [1, 4, 9, 16, 25, 36, 49, 64, 81]

def square(n):
    return n * n
square(5)
map(square, numbers)


# <map object at 0x100fe5940>
# range(10)
# range(0, 10)
list(map(square, numbers))
def first_letter(word):
    return word[0]

first_letter('Berkeley')
list(map(first_letter, words))


















words
# ['The', 'University', 'of', 'Califonria', 'at', 'Berkeley']
def is_even(n):
    return n % 2 == 0
# ...
is_even(3)
# False
 numbers
#   File "<stdin>", line 1
numbers
# IndentationError: unexpected indent
numbers
# range(0, 10)
[ n for n in numbers if is_even(n) ]
2, 4, 6, 8]
filter(is_even, numbers)
# <filter object at 0x101069b50>
list(filter(is_even, numbers))
2, 4, 6, 8]
def long_word(word):
    return len(word) > 3
# ...
long_word('of')
# False
list(filter(long_word, words))
# ['University', 'Califonria', 'Berkeley']
# >>>
# >>>
from functools import reduce
from operator import add, mul
reduce
# <built-in function reduce>
add(1, 2)
# 3
reduce(add, numbers)
# 45
list(numbers)
1, 2, 3, 4, 5, 6, 7, 8, 9]
1 + 2 +3 +4+5+6+7+8+9
# 45
result = add(0, 1)
result
# 1
result = add(result, 2)
result
# 3
result = add(result, 3)
result = add(result, 4)
result = add(result, 5)
result = add(result, 6)
result
# 21
result = add(result, 7)
result = add(result, 8)
result = add(result, 9)
result
# 45
reduce(mul, numbers)
# 0
reduce(mul, range(1, 5))
# 24
reduce(mul, range(1, 10))
# 362880
# >>>
# >>>
# >>>
# >>>
# >>>
words
# ['The', 'University', 'of', 'Califonria', 'at', 'Berkeley']
def sentence(word1, word2):
    return word1 + ' ' + word2
# ...
sentence('Hello', 'CS88')
# 'Hello CS88'
reduce(sentence, words)
# 'The University of Califonria at Berkeley'
join
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'join' is not defined
def join(word1, word2):
    return word1 + word2
# ...
# >>>







# >>>
# >>>
words
# ['The', 'University', 'of', 'Califonria', 'at', 'Berkeley']
school
# 'The University of Califonria at Berkeley'
first_letter('Berkeley')
# 'B'
long_word('The')
# False
 add('U', 'C')
#   File "<stdin>", line 1
add('U', 'C')
# IndentationError: unexpected indent
add('U', 'C')
# 'UC'
'U' + 'C'
# 'UC'
map(first_letter, words)
# <map object at 0x10103be80>
list(map(first_letter, words))
# ['T', 'U', 'o', 'C', 'a', 'B']
list(filter(long_word,  map(first_letter, words)))
# []
list(map(first_letter, filter(long_word, words)))
# ['U', 'C', 'B']
reduce(add, map(first_letter, filter(long_word, words)))
# 'UCB'
def acronym(sentence):
    words = setence.split()
    return reduce(add, map(first_letter, filter(long_word, words)))
# ...
school
# 'The University of Califonria at Berkeley'
acronym(school)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 2, in acronym
# NameError: name 'setence' is not defined
def acronym(sentence):
    words = sentence.split()
    return reduce(add, map(first_letter, filter(long_word, words)))
# ...
acronym(school)
# 'UCB'
# >>>
