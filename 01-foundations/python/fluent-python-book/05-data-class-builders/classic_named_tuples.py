### Defining and using a named tuple type

from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print( tokyo.population )

print( City._fields )

Coordinate = namedtuple('Coordinate', 'lat lon')
delhi_data = ('Delhi NCR', 'IN', 21.935, Coordinate(28.613889, 77.208889))
delhi = City._make(delhi_data)
print( delhi._asdict() )

Coordinate = namedtuple('Coordinate', 'lat lon reference', defaults=['WGS84'])
print( Coordinate(0, 0) )
print( Coordinate._field_defaults )



