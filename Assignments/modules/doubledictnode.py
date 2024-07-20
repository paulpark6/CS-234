class DoubleDictNode:
    """
    Fields: _key_one stores the value of key one (Any)
            _key_two stores the value of key two (Any)
            _parent points to the parent, if any, else None
            _left points to the left child, if any, else None
            _right points to the right child, if any, else None
            _next points to the next, if any, else None
    """

    def __init__(self, key_one, key_two, parent = None,
                 left = None, right = None, next = None):
        """
        DoubleDictNode(key_one, key_two, parent, left, right,
            next) produces a newly constructed 
            DoubleDictDNnode storing the given key_one and
            key_two, with default values of None for pointers.
        Effects: Creates a new DoubleDictNode.
        __init__: Any Any (anyof DoubleDictNode None) 
                  (anyof DoubleDictNode None) 
                  (anyof DoubleDictNode None) 
                  (anyof DoubleDictNode None) 
                  -> DoubleDictNode

        """
        self._key_one = key_one
        self._key_two = key_two
        self._parent = parent
        self._left = left
        self._right = right
        self._next = next

    def __repr__(self):
        """
        repr(self) produces a string with the information in self.
        __repr__: DoubleDictNode -> Str

        """
        return str("key_one: " + str(self._key_one) + " "
                   "key_two: " + str(self._key_two))

    def access_key_one(self):
        """
        self.access_key_one() produces key_one in self.
        access_key_one: DoubleDictNode -> Any

        """
        return self._key_one

    def access_key_two(self):
        """
        self.access_key_two() produces key_two in self.
        access_key_two: DoubleDictNode -> Any

        """
        return self._key_two
    

    def access_parent(self):
        """
        self.access_parent() produces the node to which self is linked
           using parent or None if none exists.
        access_parent: DoubleDictNode -> (anyof DoubleDictNode None)

        """
        return self._parent

    def access_left(self):
        """
        self.access_left() produces the node to which self is linked
           using left or None if none exists.
        access_left: DoubleDictNode -> (anyof DoubleDictNode None)

        """
        return self._left

    def access_right(self):
        """
        self.access_right() produces the node to which self is linked
           using right or None if none exists.
        access_right: DoubleDictNode -> (anyof DoubleDictNode None)

        """
        return self._right

    def access_next(self):
        """
        self.access_next() produces the node to which self is linked
           using next or None if none exists.
        access_next: DoubleDictNode -> (anyof DoubleDictNode None)

        """
        return self._next
    
    def store_key_one(self, key_one):
        """
        self.store_key_one(key_one) stores key_one in self.
        Effects: Mutates self by storing key_one in self.
        store_key_one: DoubleDictNode Any -> None

        """
        self._key_one = key_one

    def store_key_two(self, key_two):
        """
        self.store_key_two(key_two) stores key_two in self.
        Effects: Mutates self by storing key_two in self.
        store_key_two: DoubleDictNode Any -> None

        """
        self._key_two = key_two
        
    def link_parent(self, node):
        """
        self.link_parent(node) links node using the parent pointer,
            or None.
        Effects: Mutates self by linking node using the parent pointer, 
            or None.    
        link_parent: DoubleDictNode (anyof DoubleDictNode None) -> None

        """
        self._parent = node

    def link_left(self, node):
        """
        self.link_left(node) links node using the left pointer,
            or None.
        Effects: Mutates self by linking node using the left pointer, 
            or None.    
        link_left: DoubleDictNode (anyof DoubleDictNode None) -> None

        """
        self._left = node

    def link_right(self, node):
        """
        self.link_right(node) links node using the right pointer,
            or None.
        Effects: Mutates self by linking node using the right pointer, 
            or None.    
        link_right: DoubleDictNode (anyof DoubleDictNode None) -> None

        """
        self._right = node

    def link_next(self, node):
        """
        self.link_next(node) links node using the next pointer,
            or None.
        Effects: Mutates self by linking node using the next pointer, 
            or None.    
        link_next: DoubleDictNode (anyof DoubleDictNode None) -> None

        """
        self._next = node
        
        