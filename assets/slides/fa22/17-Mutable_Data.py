alist = [1, 2, 3, 4]
alist == [1, 2, 3, 4]
# True
alist == [1, 2, 3, 4, 5]
# False
alist == [1, 2, 4, 3]
# False
alist is [1, 2, 3, 4]
# False
blist = alist
alist is blist
# True
alist.append(5)
alist
# [1, 2, 3, 4, 5]
blist
# [1, 2, 3, 4, 5]
alist == blist
# True
alist is blist
# True
clist = list(blist)
clist
# [1, 2, 3, 4, 5]
clist is blist
# False
clist.append(6)
clist
# [1, 2, 3, 4, 5, 6]
clist == blist
# False
blist
# [1, 2, 3, 4, 5]
dlist = clist[:]
dlist is clist
# False
dlist == clist
# True
person = { 'name': 'Michael' }
person
# {'name': 'Michael'}
person['name']
# 'Michael'
person.get('name')
# 'Michael'
person['email'] = 'ball@berkeley'
person
# {'name': 'Michael', 'email': 'ball@berkeley'}
'phone' in person
# False
'name' in person
# True
'Michael' in person
# False
person.keys()
# dict_keys(['name', 'email'])
text = 'One upon a time'
text.split()
# ['One', 'upon', 'a', 'time']
{ word : len(word) for word in text.split() }
# {'One': 3, 'upon': 4, 'a': 1, 'time': 4}
words = { word : len(word) for word in text.split() }
for w in words:
    print(w)
# ...
# One
# upon
# a
# time
for w, l in words.items():
    print(w, l)
# ...
# One 3
# upon 4
# a 1
# time 4
words['there'] = 5
words
# {'One': 3, 'upon': 4, 'a': 1, 'time': 4, 'there': 5}
d = { 'a': 'b', 'hello': True }
d[ [1, 2] ] = 5
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unhashable type: 'list'
d[(1,2,3)] = 'cool'
d
# {'a': 'b', 'hello': True, (1, 2, 3): 'cool'}
counter = 0
def counter_fun():
    counter += 1
    return counter
# ...
counter_fun()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 2, in counter_fun
# UnboundLocalError: local variable 'counter' referenced before assignment
counter
# 0
counter = 10
def make_counter():
    counter = [0]
    def counts():
            counter[0] += 1
            return counter
    return counts
# ...
c = make_counter()
c
# <function make_counter.<locals>.counts at 0x10ce88ee0>
c()
# 1
c()
# 2
c()
# 3
second = make_counter()
second
# <function make_counter.<locals>.counts at 0x10ce88f70>
second()
# 1
second()
# 2
second()
# 3
c()
# 4

def add_data_to_obj(obj, data):
     print(obj)
     obj += data
     print(obj)
     return obj

def new_obj_with_data(obj, data):
     print(obj)
     obj = obj + data
     print(obj)
     return obj



def make_withdraw_account(initial):
    balance = [initial]

    def withdraw(amount):
        if balance[0] - amount < 0:
            return 'Insufficient funds'
        balance[0] -= amount
        return balance[0]
    return withdraw


withdraw = make_withdraw_account(100)
withdraw(25)
withdraw(25)
withdraw(25)
withdraw(50)
