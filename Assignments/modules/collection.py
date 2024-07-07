class Collection:
    """
    Fields: _contents contains data items

    """

    def __init__(self):
        """
        Collection() produces a new, empty collection.
        Effects: Creates a new, empty collection.
        __init__: -> Collection

        """
        self._contents = []


    def __repr__(self):
        """
        repr(self) produces a string of the data stored.
        __repr__: Collection -> Str

        """
        return repr(self._contents)

    def is_empty(self):
        """
        self.is_empty() produces True if self is empty and
            False otherwise.
        value: Collection -> Bool
 
        """
        return self._contents == []

    def add(self, item):
        """
        self.add(item) adds item to self.
        Effects: Adds item to self
        add: Collection -> None

        """
        self._contents.append(item)
    
    def delete_any(self):
        """
        self.delete_any() produces an item and removes it from self.
        Effects: Removes an item from self
        delete_any: Collection -> Any
        Requires: self is nonempty

        """
        return self._contents.pop()
                

