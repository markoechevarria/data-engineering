## Dictionaries and sets


Dictionaries supports pattern matching

collections.abc module provides the Mapping and MutableMapping ABCs describing the interfaces of dict and similar types.

All mapping class must have the key hashable, the values need not be.

setdefault method can update items holding mutable values
update method allows builk insertion or overwritting of items

collections.defauldict creates items with a default value whenever a missing key is searched using d[k] syntax.

It is better to create a new mapping type by extending collections.UserDict rather than dict.

collections.OrderedDict -> designed to be good at reordering operations
collections.ChainMap -> holds a list of mapping that can be searches as one
collections.Counter -> holds an integer count for each key
shelve.Shelf -> persistent storage for a mapping of string keys to python objects serialized in the pickly binary format

collections.MappingProxyType return a unmatable mapping which cannnot update the content

Dictionary views -> read-only projections of the internal data structures used in the dict implementation.

## How dict works

* key must be hashable objets ( must implement __hash__ and __eq__ )
* Item access by key is very fast
* Key ordering is preserved
* Dicts inevitably have a significant memory overhead, a hash table need to store data per entry, and its neccesary keep at least one-third of the hash table rows empty.
* To save memory, avoid creating instances attributes outside of the __init__ method

## How sets works

* set elements must be hashable objets ( __hash and __eq__ )
* Membership testing is efficient
* Set have a significant memory overhead.
* Element ordering dependes on insertinon order.
* Adding elements to a set may change the oder of existing elements.
