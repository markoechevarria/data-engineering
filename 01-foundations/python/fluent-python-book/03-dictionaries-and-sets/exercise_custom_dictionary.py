from collections.abc import Mapping

class CaseInsensitiveDict:

    def __init__(self, data):

        if not isinstance(data, Mapping):
            raise TypeError

        self._data = { key.lower(): (key, value) for key, value in data.items() if isinstance(key, str)}

    def __str__(self):

        return f"{self._data}"

    def __repr__(self):
        return f"CaseInsensitiveDict{self._data}"

    def __getitem__(self, key):

        if not isinstance(key, str):
            raise TypeError

        return self._data[key.lower()][-1]

    def get(self, key, default=None):

        if not isinstance(key, str):
            raise TypeError

        return self._data.get(key.lower(), default)

    def __setitem__(self, key, value):

        if not isinstance(key, str):
            raise TypeError

        self._data[key.lower()] = (key, value)

    def __len__(self):

        return len(self._data)

    def __delitem__(self, key):

        if not isinstance(key, str):
            raise TypeError

        del self._data[key.lower()]

    def update(self, data):

        if not isinstance(data, Mapping):
            raise TypeError

        for key, value in data.items():
            self._data[key.lower()] = (key, value)

    def __contains__(self, key):

        if not isinstance(key, str):
            raise TypeError

        return key.lower() in self._data

    def __iter__(self):

        return iter ( value[0] for value in self._data.values()  ) 

if __name__ == "__main__":

    data = {
        "Content-Type": "application/json"
    }

    new_data = {
        "Content-Type": "application/json",
        "noseQuePoner": "aea",
        "iDontKnow": "meNeither"
    }

    cid = CaseInsensitiveDict(data)

    a = cid["Content-Type"]

    cid["Content-Type"] = "gaaaa"
    b = cid["Content-Type"]
    c = "Content-Type" in cid 
    d = cid.get("Content-Type")
    cid.update(new_data)
    e = cid
    f = cid["content-Type"]
    g = cid["CONTENT-TYPE"]

    print( a )
    print( b )
    print( c )
    print( d )
    print( e )
    for item in cid: print( item )
    print( f )
    print( g )
