### MappingProxyType

from types import MappingProxyType

d = {1: 'A'}
d_proxy = MappingProxyType(d)
d_proxy[1]

d[2] = 'B'
print( d_proxy )
print( d_proxy[2] )

### Dictionary Views: Views are read-only projections. A view object is a dynamic proxy

d = dict(a=10, b=20, c=30)
values = d.values()
print( values )
print( len(values) )
print( list(values) )
print( reversed(values) )
# print( values[0] )

### Set Theory

l = ['spam', 'eggs', 'spam']
print( set(l) )

s = {1}
print( type(s) )
print( s )
s.pop()
print( s )

frozen = frozenset([1,2,3,4,5])

### Set Comprehensions

from unicodedata import name

signs = { chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i),'')}
print(signs)
