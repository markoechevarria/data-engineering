### __missing__ method

class StryKeyDict0(dict):

    def __misssing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()

### __missing__ method inconsistents

class DictSubclass(dict):

    def __missing__(self, key):
        print("__missing__ is called")
        return None

from collections import UserDict
from collections.abc import Mapping

class UserDictSubclass(UserDict):
    def __missing__(self, key):
        print("__missing__ is called")
        return None

class MappingSubclass(Mapping):

    def __init__(self, *args, **kwargs):
        self._data = dict(*args, **kwargs)

    def __getitem__(self, key):
        return self._data[key]

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        return iter(self._data)

    def __missing__(self, key):
        print("__missing__ is called")
        return None

class DoubleMappingSubclass(MappingSubclass):

    def __getitem__(self, key):
        try:
            return self._data[key]
        except KeyError:
            return None


dictSubclass = DictSubclass({'a': 1, 'b': 2})
print( "=== dict ===" ) 
print( dictSubclass['a'] )
print( dictSubclass['c'] )

userdictSubclass = UserDictSubclass({'a': 1, 'b': 2})
print( "=== collections.UserDict ===" ) 
print( userdictSubclass['a'] )
print( userdictSubclass['c'] )

mappingSubclass = MappingSubclass({'a': 1, 'b': 2})
print( "=== abc.Mapping ===" ) 
print( mappingSubclass['a'] )
print( mappingSubclass['c'] )

doublemappingSubclass = DoubleMappingSubclass({'a': 1, 'b': 2})
print( "=== abc.Mapping double ===" ) 
print( doublemappingSubclass['a'] )
print( doublemappingSubclass['c'] )
