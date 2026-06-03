###

### Mutable Instances

collections.namedtuple and typing.NamedTuple build tuple subclasses ( inmutables ), @dataclass produces mutable classes ( frozen=True make it inmutable )

### Class statement syntax

Only typing.NamedTuple and dataclass support the regular case statement syntax

### Construct dict

Both named tuple variants provide an instance method ( ._asdict ) to construct a dic object from teh fields in a data class instance.
The dataclasses module provides a function to do it: dataclasses.asdict

### get field names and default values

In named tuples classes ._fields and ._fields_defaults allow get field names and default values
In a data class decorated class use .fields

### Get field types

typing.NamedTuple and @dataclass have a mapping of fields names to type the __annotations__ class atribute, use the function typing.get_type_hints

### New instance with changes

x.replace(**kwargs) returns a new instance with some attribute values replaced
dataclasses.replace(x, **kwargs) does the same for dataclass decorated class

### New class at runtime

To build data classes at runtime use the function call of collections.namedtuple, dataclasses module provides a make_class function

## Classic Named Tuples

* collections.namedtuple builds subclasses of tuple enhanced with fields names, a class name, and __repr__
* Its possible to add methods to a namedtuple

## Typed Named Tuples

* Classes built by typing.NamedTuple don't have any methods beyond those that collections.namedtuple also generates. The only difference is the presence of the __annotations__ class attribute

## Data class as a code smell

* Data class as scaffolding -> the data class is an initial, simplistic implementation of a class
* Data class as Intermediate Representation -> a data class can be useful to build records about to be exported to JSON or some other interchange format, in this scenario, the data class instances should be handled as inmutable objects





