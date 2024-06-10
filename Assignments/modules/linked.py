## @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
##   
##   CS 234 code download
##   Version date: March 2022
##   File name: linked.py
##   
## @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
##
## Classes implementing different types of nodes for linked data structures
##
class Single:
    """
    Fields: _value stores any value
            _next stores the next node or None, if none
    """

    def __init__(self, value, next = None):
        """
        Single(value, next) produces a newly constructed singly-linked 
           node storing value with a link to next, where next has the
           default value None.
        Effects: Creates a new Single.
        __init__: Any (anyof Single None) -> Single

        """
        self._value = value
        self._next = next

    def __repr__(self):
        """
        repr(self) produces a string with the information in self.
        __repr__: Single -> Str

        """
        if self._value is None:
            return "Empty node"
        else:
            return str("Node containing " + str(self._value))

    def access(self):
        """
        self.access() produces the value stored in self.
        access: Single -> Any

        """
        return self._value

    def next(self):
        """
        self.next() produces the node to which self is linked
           or None if none exists.
        next: Single -> (anyof Single None)

        """
        return self._next

    def store(self, value):
        """
        self.store(value) stores value in self.
        Effects: Mutates self by storing value in self.
        store: Single Any -> None

        """
        self._value = value

    def link(self, node):
        """
        self.link(node) links node using the next pointer.
        Effects: Mutates self by linking node using the next pointer.    
        link: Single (anyof Single None) -> None

        """
        self._next = node

class Double:
    """
    Fields: _value stores any value
            _next points to the next node in the list
            _prev points to the previous node in the list
    """

    def __init__(self, value, next = None, prev = None):
        """
        Double(value, next, prev) produces a newly constructed
            doubly-linked node storing value with a next pointer
            to next and a prev pointer to prev, where next and prev
            have the default values of None.
        Effects: Creates a new Double.
        __init__: Any (anyof Double None) (anyof Double None) -> Double

        """
        self._value = value
        self._next = next
        self._prev = prev

    def __repr__(self):
        """
        repr(self) produces a string with the information in self.
        __repr__: Double -> Str

        """
        if self._value is None:
            return "Empty node"
        else:
            return str("Node containing " + str(self._value))

    def access(self):
        """
        self.access() produces the value stored in self.
        access: Double -> Any

        """
        return self._value

    def next(self):
        """
        self.next() produces the node to which self is linked
           using next or None if none exists.
        next: Double -> (anyof Double None)

        """
        return self._next

    def prev(self):
        """
        self.prev() produces the node to which self is linked
           using prev or None if none exists.
        prev: Double -> (anyof Double None)

        """
        return self._prev

    def store(self, value):
        """
        self.store(value) stores value in self.
        Effects: Mutates self by storing value in self.
        store: Double Any -> None

        """
        self._value = value

    def link_next(self, node):
        """
        self.link_next(node) links node using the next pointer.
        Effects: Mutates self by linking node using the next pointer.    
        link_next: Double (anyof Double None) -> None

        """
        self._next = node

    def link_prev(self, node):
        """
        self.link_prev(node) links node using the prev pointer.
        Effects: Mutates self by linking node using the prev pointer.
        link_prev: Double (anyof Double None) -> None

        """
        self._prev = node
        
