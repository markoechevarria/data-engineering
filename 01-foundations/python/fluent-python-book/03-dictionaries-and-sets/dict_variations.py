### collections.OrderedDict -> keeps the keys ordered, was designed to be good at reordering operations.

### collections.ChainMap -> holds a list of mappings. Perform a lookup in the order each input appears in the constructor call.

d1 = dict(a=1, b=3)
d2 = dict(a=2, b=4, c=6)

from collections import ChainMap

chain = ChainMap(d1, d2)
print( chain['a'] )
print( chain['c'] )

### collections.Counter -> Holds an integer count for each key

from collections import Counter

ct = Counter('abracadabra')
print(ct)
ct.update('aaaaaaazzzz')
print(ct)
print(ct.most_common(3))

### shelve.Shelf -> persistent storage for a mapping of string keys to Python objects serialized in the pickly binary format.

### UserDict -> better subcast from 

from collections import UserDict
class StrKeyDict(UserDict):

    def __missing__(self, key):
        if isinstance(key, str):
            return KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data

    def __setitem__(self, key, item):
        self.data[str(key)] = item



