from collections import defaultdict

class MemoryTaggingEngine:

    def __init__(self, data):
        self.data = data

        self.inverted = defaultdict(set)

        for key, value in self.data.items():
            for word in value.split():
                self.inverted[word].add(key)

    def inverted_index(self):

        return dict(self.inverted)

    def search_any(self, words):

        sets = [ self.inverted.get(word, set()) for word in words ]
        return set.union(*sets)

    def search_all(self, words):

        sets = [ self.inverted.get(word, set()) for word in words ]
        return set.intersection( *sets )

    def search_exactly_one(self, words):

        sets = [ self.inverted.get(word, set()) for word in words ]
        return set.symmetric_difference( *sets )

if __name__ == "__main__":

    documents = {
        1: "python dictionaries are powerful",
        2: "sets are useful for fast membership tests",
        3: "python supports powerful comprehensions",
        4: "membership tests can use sets or dictionaries",
    }

    mt = MemoryTaggingEngine(documents)
    a = mt.inverted_index()
    b = mt.search_any(["python", "are"])
    c = mt.search_all(["python", "are"])
    d = mt.search_exactly_one(["python", "are"])

    print(a)
    print(b)
    print(c)
    print(d)
