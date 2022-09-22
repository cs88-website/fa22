
def say_hi(name):
    print(f'Hi, {name}')

say_hi = lambda name: print(f'Hi, {name}')

sorted([5, 4, 3, 2, 1])

# This is the "identity" function
sorted([5, 4, 3, 2, 1], key = lambda x: x)

sorted([1,2,3,4,5], key = lambda x: -x)

sorted([(2, "hi"), (1, "how"), (5, "goes"), (7, "I")], key = lambda x:x[0])

sorted([(2, "hi"), (1, "how"), (5, "goes"), (7, "I")], key = lambda x:x[1])

sorted([(2,"hi"),(1,"how"),(5,"goes"),(7,"I")], key =lambda x: len(x[1]))

staff = ['Karim', 'Tommy', 'Amit', 'Hetal', 'Lukas', 'Michelle', 'Joanna',
    'Anjali', 'Jessica', 'Michael', 'Ethan', 'Sebastian', 'Christine']

sorted(staff)

# More practice with map / filter / reduce
remove_dupes = lambda result, data: result if data in result else result + [ data ]

from functools import reduce

reduce(remove_dupes, staff, [])

course = {
    'name': 'Comp Structures in Data Science',
    'number': 'C88C',
    'room': '105 Stanley Hall'
}

text = 'Once Upon A Time'

counts  = { word : len(word) for word in text.split(' ') }
counts

counts.keys()
counts.values()
counts.items()
# counts['time']
# counts['hello']
counts.get('hello')
