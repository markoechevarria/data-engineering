from typing import NamedTuple

class Coordinate(NamedTuple):
    lat: float
    lon: float
    reference: str = 'WGS84'

### Variable annotations

class DemoPlainClass:
    a: int
    b: float = 1.1
    c = 'spam'

print( DemoPlainClass.__annotations__ )
print( DemoPlainClass.b )

### tying.NamedTuple

class DemoNTClass(NamedTuple):
    a: int
    b: float = 1.1
    c = 'spam'

print( DemoNTClass.a )
print( DemoNTClass.b )
print( DemoNTClass.c )

### dataclasses.dataclass

from dataclasses import dataclass

@dataclass
class DemoDataClass:
    a: int
    b: float = 1.1
    c = 'span'

print( DemoDataClass.a )
print( DemoDataClass.b )
print( DemoDataClass.c )
