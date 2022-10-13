Last login: Mon Mar  8 01:39:15 on ttys006

michael at Catalina-Pro in ~
👉 python3
Python 3.9.1 (default, Feb  3 2021, 07:04:15) 
[Clang 12.0.0 (clang-1200.0.32.29)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> "H
  File "<stdin>", line 1
    "H
      ^
SyntaxError: EOL while scanning string literal
>>> "H" < "h"
True
>>> [ x * x for x in range(10) ]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> numbers = { 1: 1, 2: 4, 3: 9}
>>> numbers
{1: 1, 2: 4, 3: 9}
>>> numbers[3]
9
>>> 
>>> 
>>> [ x * x for x in range(10) ]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> { x : x * x for x in range(10) }
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
>>> my_dict = { x : x * x for x in range(10) }
>>> my_dict[5]
25
>>> 5 in my_dict
True
>>> 25 in my_dict
False
>>> my_dict = {str(x) : x * x for x in range(10) }
>>> my_dict
{'0': 0, '1': 1, '2': 4, '3': 9, '4': 16, '5': 25, '6': 36, '7': 49, '8': 64, '9': 81}
>>> { letter : 0 for letter in 'Hello, CS88' }
{'H': 0, 'e': 0, 'l': 0, 'o': 0, ',': 0, ' ': 0, 'C': 0, 'S': 0, '8': 0}
>>> sentence = 'Once upon a time there was'
>>> words = sentence.split(' ')
>>> words
['Once', 'upon', 'a', 'time', 'there', 'was']
>>> counts = {}
>>> for word in words:
...     counts[word] = len(word)
... 
>>> counts
{'Once': 4, 'upon': 4, 'a': 1, 'time': 4, 'there': 5, 'was': 3}
>>> { word : len(word) for word in words }
{'Once': 4, 'upon': 4, 'a': 1, 'time': 4, 'there': 5, 'was': 3}
>>> { word : word for word in words }
{'Once': 'Once', 'upon': 'upon', 'a': 'a', 'time': 'time', 'there': 'there', 'was': 'was'}
>>> sq = lambda i : i * i
>>> sq(4)
16
>>> [ sq for x in range(4) ]
[<function <lambda> at 0x109825a60>, <function <lambda> at 0x109825a60>, <function <lambda> at 0x109825a60>, <function <lambda> at 0x109825a60>]
>>> [ lambda i : i*i  for x in range(4) ]
[<function <listcomp>.<lambda> at 0x1098254c0>, <function <listcomp>.<lambda> at 0x109825820>, <function <listcomp>.<lambda> at 0x109825d30>, <function <listcomp>.<lambda> at 0x109825e50>]
>>> [ (lambda i : i*i)(x)  for x in range(4) ]
[0, 1, 4, 9]
>>> [ sq(x)  for x in range(4) ]
[0, 1, 4, 9]
>>> wordcount = lambda words: { word : len(word) for word in words }
>>> 
>>> word
word        wordcount(  words       
>>> wordcount(
... 
KeyboardInterrupt
>>> wordcount
<function <lambda> at 0x1098254c0>
>>> wordcount(words)
{'Once': 4, 'upon': 4, 'a': 1, 'time': 4, 'there': 5, 'was': 3}
>>> [x + y  for x in range(0, 10, 2) for y in range(1, 10, 2)] #when len(list1) == len(list2)
[1, 3, 5, 7, 9, 3, 5, 7, 9, 11, 5, 7, 9, 11, 13, 7, 9, 11, 13, 15, 9, 11, 13, 15, 17]
>>> [print(f'X: {x}, Y: {y}, x+y: {x+y}')  for x in range(0, 10, 2) for y in range(1, 10, 2)] #when len(list1) == len(list2)
X: 0, Y: 1, x+y: 1
X: 0, Y: 3, x+y: 3
X: 0, Y: 5, x+y: 5
X: 0, Y: 7, x+y: 7
X: 0, Y: 9, x+y: 9
X: 2, Y: 1, x+y: 3
X: 2, Y: 3, x+y: 5
X: 2, Y: 5, x+y: 7
X: 2, Y: 7, x+y: 9
X: 2, Y: 9, x+y: 11
X: 4, Y: 1, x+y: 5
X: 4, Y: 3, x+y: 7
X: 4, Y: 5, x+y: 9
X: 4, Y: 7, x+y: 11
X: 4, Y: 9, x+y: 13
X: 6, Y: 1, x+y: 7
X: 6, Y: 3, x+y: 9
X: 6, Y: 5, x+y: 11
X: 6, Y: 7, x+y: 13
X: 6, Y: 9, x+y: 15
X: 8, Y: 1, x+y: 9
X: 8, Y: 3, x+y: 11
X: 8, Y: 5, x+y: 13
X: 8, Y: 7, x+y: 15
X: 8, Y: 9, x+y: 17
[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
>>> for x in range(0, 10, 2):
...     for y in range(1, 10, 2):
...             print(f'X: {x}, y: {y}, x+y: {x+y}')
... 
X: 0, y: 1, x+y: 1
X: 0, y: 3, x+y: 3
X: 0, y: 5, x+y: 5
X: 0, y: 7, x+y: 7
X: 0, y: 9, x+y: 9
X: 2, y: 1, x+y: 3
X: 2, y: 3, x+y: 5
X: 2, y: 5, x+y: 7
X: 2, y: 7, x+y: 9
X: 2, y: 9, x+y: 11
X: 4, y: 1, x+y: 5
X: 4, y: 3, x+y: 7
X: 4, y: 5, x+y: 9
X: 4, y: 7, x+y: 11
X: 4, y: 9, x+y: 13
X: 6, y: 1, x+y: 7
X: 6, y: 3, x+y: 9
X: 6, y: 5, x+y: 11
X: 6, y: 7, x+y: 13
X: 6, y: 9, x+y: 15
X: 8, y: 1, x+y: 9
X: 8, y: 3, x+y: 11
X: 8, y: 5, x+y: 13
X: 8, y: 7, x+y: 15
X: 8, y: 9, x+y: 17
>>> counts
{'Once': 4, 'upon': 4, 'a': 1, 'time': 4, 'there': 5, 'was': 3}
>>> counts.keys()
dict_keys(['Once', 'upon', 'a', 'time', 'there', 'was'])
>>> for key in counts.keys():
...     print(key)
... 
Once
upon
a
time
there
was
>>> for value in couts.values():
...     print(value)
... 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'couts' is not defined
>>> for value in counts.values():
...     print(value)
... 
4
4
1
4
5
3
>>> counts.items()
dict_items([('Once', 4), ('upon', 4), ('a', 1), ('time', 4), ('there', 5), ('was', 3)])
>>> counts.items()[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'dict_items' object is not subscriptable
>>> items = list(counts.items())
>>> items
[('Once', 4), ('upon', 4), ('a', 1), ('time', 4), ('there', 5), ('was', 3)]
>>> items[0]
('Once', 4)
>>> key, value = 0, 1
>>> key
0
>>> value
1
>>> key, value = items
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: too many values to unpack (expected 2)
>>> key, value = items[0]
>>> key
'Once'
>>> value
4
>>> for key, value in counts.items():
...     print(key, value)
... 
Once 4
upon 4
a 1
time 4
there 5
was 3
>>> for key in counts:
...     print(key, counts[key])
... 
Once 4
upon 4
a 1
time 4
there 5
was 3
>>> counts
{'Once': 4, 'upon': 4, 'a': 1, 'time': 4, 'there': 5, 'was': 3}
>>> items
[('Once', 4), ('upon', 4), ('a', 1), ('time', 4), ('there', 5), ('was', 3)]
>>> items[0]
('Once', 4)
>>> items[0][0]
'Once'
>>> items[0][1]
4
>>> counts.items()
dict_items([('Once', 4), ('upon', 4), ('a', 1), ('time', 4), ('there', 5), ('was', 3)])
>>> type counts.items()
  File "<stdin>", line 1
    type counts.items()
         ^
SyntaxError: invalid syntax
>>> type(counts.items())
<class 'dict_items'>
>>> type([])
<class 'list'>
>>> type(4)
<class 'int'>
>>> type(counts.keys())
<class 'dict_keys'>
>>> 
