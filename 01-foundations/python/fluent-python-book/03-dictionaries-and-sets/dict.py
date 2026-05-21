dial_codes = [
        (880, 'Bangladesh'),
        (55, 'Brazil'),
        (86, 'China'),
        (91, 'India'),
        (62, 'Indonesia')
]

country_dial = {code: country.upper() for code, country in dial_codes if code < 90}
print(country_dial)

def dump(**kwargs):
    print( kwargs )

dump(**{'x': 1}, y=2, **{'z': 3})

dicty = {'a': 0, **{'x': 1}, 'y': 2, **{'z': 3, 'x': 4}}
print( dicty )

d1 = {'a': 1, 'b': 3}
d2 = {'a': 2, 'c': 4, 'd': 5}
print( d1 | d2 )

d1 |= d2
print(d1)

def get_creators(record: dict) -> list:
    match record:
        case {'type': 'book', 'api': 2, 'authors': [*names]}:
            return names
        case {'type': 'book', 'api': 1, 'author': name}:
            return [name]
        case {'type': 'book'}:
            raise ValueError()
        case {'type': 'movie', 'director': name}:
            return [name]
        case _:
            raise ValueError(f'Invalid record: {record!r}')

""" index mapping word """

import re

WORD_RE = re.compile(r'\w+')

index = {}

text = """
Lorem Ipsum is simply dummy text of the printing and typesetting
industry. Lorem Ipsum has been the industry's standard dummy
text ever since the 1500s, when an unknown printer took a galley
of type and scrambled it to make a type specimen book. It has
survived not only five centuries, but also the leap into electronic
typesetting, remaining essentially unchanged. It was popularised in
the 1960s with the release of Letraset sheets containing Lorem
Ipsum passages, and more recently with desktop publishing
software like Aldus PageMaker including versions of Lorem Ipsum.
""".split("\n")

for line_no, line in enumerate(text, 1):
    for match in WORD_RE.finditer(line):
        word = match.group()
        column_no = match.start() + 1
        location = (line_no, column_no)
        index.setdefault(word, []).append(location)

for word in sorted(index, key=str.upper):
    print( word, index[word] )



