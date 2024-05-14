## A class implementing Counter

## Note that data types of items must be immutable.

class Counter:
    """
    Fields: _data contains the items
    """

    ## Counter() produces a newly constructed empty counter.
    ## __init__:  -> Counter
    def __init__(self):
        self._data = {}

    ## repr(self) produces a string of values stored in self.
    ## __repr__: Counter -> Str
    def __repr__(self):
        return repr(self._data)

    ## self == other produces True if self and other contain the
    ##     same values and the same number of each, otherwise False.
    ## __eq__: Counter Counter -> Bool
    def __eq__(self, other):
        if not isinstance(other, Counter):
            return False
        for value in self._data.keys():
            if value in other:
                self_count = self.count(value)
                other_count = other.count(value)
                if self_count != other_count:
                    return False
            else:
                return False
        for value in other.all():
            if value not in self._data.keys():
                return False
        return True
    
    ## value in self produces True if value is an item in self.
    ## __contains__: Counter Any -> Bool
    def __contains__(self, value):
        return value in self._data.keys()

    ## self.count(value) produces the number of copies of value
    ##     stored in self.
    ## count: Counter Any -> Int
    def count(self, value):
        if value in self._data.keys():
            return self._data[value]
        else:
            return 0

    ## self.all() produces a list of all distinct values in self.
    ## all: Counter -> (listof Any)
    def all(self):
        return list(self._data.keys())
    
    ## self.add(value) adds a copy of value to self.
    ## Effects: Mutates self by adding a copy of value to self.
    ## add: Counter Any -> None
    def add(self, value):
        if value in self._data.keys():
            self._data[value] = self._data[value] + 1
        else:
            self._data[value] = 1
    
    ## self.delete(value) removes a copy of value from self.
    ## Effects: Mutates self by removing a copy of value from self.
    ## delete: Counter Any -> None
    ## Requires: self contains an item with value value
    def delete(self, value):
        if self.count(value) > 1:
            self._data[value] = self._data[value] - 1
        else:
            del self._data[value]