## Simple Class Patterns

x = 123.24

match x:
    case float():
        print( "float" )

something = [ 'marko', 12, True, (123.23, 123.12)]

match something:
    case [str(name), _, _, ( float(lat), float(lon) )]:
        print( "match" )

## Keyword Class Patterns

import typing

class City(typing.NamedTuple):
    continent: str
    name: str
    country: str

cities = [
    City('Asia', 'Tokyo', 'JP'),
    City('Asia', 'Delhi', 'IN'),
    City('North America', 'Mexico City', 'MX'),
    City('North America', 'New York', 'US'),
    City('South America', 'São Paulo', 'BR'),
]


def match_asian_cities():
    results = []
    for city in cities:
        match city:
            case City(continent='Asis', country=cc):
                results.append(cc)
    return results

def match_asian_cities_pos():
    result = []
    for city in cities:
        match city:
            case City('Asia'):
                result.append(city)

def match_asian_cities_pos():
    result = []
    for city in cities:
        match city:
            case City('Asia', _, country):
                result.append(country)


