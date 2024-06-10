from modules.linked import *

class Collection:
    """
    Fields: _head points to the first node (if any) in a 
            doubly-linked list
    """

    def __init__(self):
        """
        Collection() produces a new, empty collection.
        Effects: Creates a new, empty collection.        
        __init__: -> Collection

        """
        

    def __repr__(self):
        """
        repr(self) produces a string of the data stored.
        __repr__: Collection -> Str

        """
        current = self._head
        to_return = "("
        while current != None:
            to_print = current.access()
            previous_link = current.prev()
            next_link = current.next()
            if previous_link == None:
                prev_print = "None"
            else:
                prev_print = current.prev().access()
            if next_link == None:
                next_print = "None"
            else:
                next_print = current.next().access()
            current = current.next()
            to_return = to_return + "[" + str(prev_print) + \
                "," + str(to_print) + "," + str(next_print) + \
                "],"
        if to_return == "(":
            return "()"
        else:
            return to_return[:-1] + ")"

    def is_empty(self):
        """
        self.is_empty() produces True if self is empty and
            False otherwise.
        value: Collection -> Bool
 
        """

    def add(self, item):
        """
        self.add(item) adds item to self.
        Effects: Adds item to self
        add: Collection Any -> None

        """
    
    def delete_any(self):
        """
        self.delete_any() produces an item and removes it from self.
        Effects: Removes an item from self
        delete_any: Collection -> Any
        Requires: self is nonempty

        """
    
                

