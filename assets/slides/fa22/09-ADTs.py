course = {
    'name': 'Comp Structures in Data Science',
    'number': 'C88C',
    'room': '105 Stanley Hall'
}

text = 'Once Upon A Time'

counts = { word : len(word) for word in text.split(' ') }
counts

counts.keys()
counts.values()
counts.items()
# counts['time']
# counts['hello']
counts.get('hello')
