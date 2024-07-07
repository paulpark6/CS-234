class TreeNode:
    """
    Fields: _value stores any value (Any)
            _height stores the height of the node (Int)
            _prev points to the parent (if self is first child),
                the previous sibling (if self is not first child), 
                else None
            _next points to next sibling, if any, else None
            _first points to the first child, if any, else None
    """

    def __init__(self, value, height = 0, prev_node = None, \
                 next_node = None, first_node = None):
        """
        TreeNode(value, height, prev_node, next_node, first_node)
            produces a newly constructed TreeNode storing the given
            value, with height 0 and all pointers set to None.
        Effects: Creates a new TreeNode
        __init__: Any Int (anyof TreeNode None) 
                  (anyof TreeNode None) (anyof TreeNode None) 
                   -> TreeNode

        """
        self._value = value
        self._height = 0
        self._prev = prev_node
        self._next = next_node
        self._first = first_node

    def __repr__(self):
        """
        repr(self) produces a string with the information in self.
        __repr__: TreeNode -> Str

        """
        return str("value: " + str(self._value))


    def access_value(self):
        """
        self.access() produces the value stored in self.
        access: TreeNode -> Any

        """
        return self._value

    def access_height(self):
        """
        self.access_height() produces the height stored in self.
        access: TreeNode -> Int

        """
        return self._height
    

    def access_prev(self):
        """
        self.access_prev() produces the node to which self is 
           linked using prev or None if none exists.
        access_prev: TreeNode -> (anyof TreeNode None)

        """
        return self._prev

    def access_next(self):
        """
        self.access_next() produces the node to which self is 
           linked using next or None if none exists.
        access_next: TreeNode -> (anyof TreeNode None)

        """
        return self._next

    def access_first(self):
        """
        self.access_first() produces the node to which self is 
           linked using first or None if none exists.
        access_first: TreeNode -> (anyof TreeNode None)

        """
        return self._first

    def store_value(self, value):
        """
        self.store_value(value) stores value in self.
        Effects: Mutates self by storing value in self
        store_value: TreeNode Any -> None

        """
        self._value = value

    def store_height(self, height):
        """
        self.store_height(height) stores height in self.
        Effects: Mutates self by storing height in self
        store_height: TreeNode Int -> None

        """
        self._height = height
        
    def link_prev(self, node):
        """
        self.link_prev(node) links node using the 
            prev pointer or None.
        Effects: Mutates self by linking node using the 
            prev pointer or None.    
        link_prev: TreeNode (anyof TreeNode None) -> None

        """
        self._prev = node
        
    def link_next(self, node):
        """
        self.link_next(node) links node using the 
            next pointer or None.
        Effects: Mutates self by linking node using the 
            next pointer or None    
        link_next: TreeNode (anyof TreeNode None) -> None

        """
        self._next = node

    def link_first(self, node):
        """
        self.link_first(node) links node using the 
            first pointer or None.
        Effects: Mutates self by linking node using the 
            first pointer or None    
        link_first: TreeNode (anyof TreeNode None) -> None

        """
        self._first = node

        
        
        