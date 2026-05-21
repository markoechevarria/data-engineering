### with collections.namedtuple

from collections import namedtuple

Coordinate = namedtuple('Coordinate', 'lat lon')
moscow = Coordinate(55.766, 37.617)

### with typing.NamedTuple

import typing

Coordinate = typing.NamedTuple('Coordinate', [('lat', float), ('long', float)]) ## also can use lat=float, lon=float
typing.get_type_hints(Coordinate)

### typing.NamedTuple used in a class statement

from typing import NamedTuple

class Coordinate(NamedTuple):
    lat: float
    lon: float

    def __str__(self):

        ns = 'N' if self.lat >= 0 else 'S'
        we = 'E' if self.lon >= 0 else 'W'

        return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'

moscow = Coordinate(55.766, 37.617)
print( moscow )

### Using dataclass

from dataclasses import dataclass

@dataclass(frozen=True)
class Coordinate:
    lat: float
    lon: float

    def __str__(self):

        ns = 'N' if self.lat >= 0 else 'S'
        we = 'E' if self.lon >= 0 else 'W'

        return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'

moscow = Coordinate(55.766, 37.617)
print( moscow )

