from doubledictnode import *

class DoubleDict:
    """
    Fields: _root is the root doubledictnode for the
                BST based on key_one, if any, or None
                if the double dictionary is empty
            _head is the first doubledictnode in the
                ordered linked list based on key_two,
                if any, or None if the double dictionary 
                is empty
            key_one is a string and key_two is an integer
    """

    def __init__(self):
        """
        DoubleDict() produces an empty doubledict.
        Effects: Create a new, empty doubledict.
         __init__: -> DoubleDict

        """

    def __repr__(self):
        """
        repr(self) produces a string with the information in
            the linked list of self.
        __repr__: DoubleDict -> Str

        """
        part_two = ""
        current = self._head
        while current != None:
            part_two = part_two + repr(current) + " "
            current = current.access_next()
        return part_two

    def tree_repr(self, node):
        """
        self.tree_repr(node) produces a string with the 
            information rooted at node in the BST of
            self.
        tree_repr: DoubleDict -> Str
        Requires: node is a node in the BST of self

        """
        to_return = repr(node)
        if node._left != None:
            to_return = to_return + " Left subtree " + \
                self.tree_repr(node._left)
        else:
            to_return = to_return + " No left subtree "
        if node._right != None:
            to_return = to_return + " Right subtree " + \
                self.tree_repr(node._right)
        else:
            to_return = to_return + " No right subtree "
        return to_return
    
    def is_empty(self):
        """    
        self.is_empty() produces True if the double 
            dictionary is empty and False otherwise.
        is_empty: DoubleDict -> Bool
        
        """

    def look_up_one(self, key_one):
        """
        self.look_up_one(key_one) produces the 
            key_two stored with key_one, if any,
            and False otherwise.
        look_up_one: DoubleDict Str 
            -> (anyof Int False)

        """
            
    def look_up_two(self, key_two):
        """
        self.look_up_two(key_two) produces the 
            key_one stored with key_two, if any,
            and False otherwise.
        look_up_two: DoubleDict Int 
            -> (anyof Str False)

        """

    def add_one(self, key_one, key_two):
        """
        self.add_one(key_one, key_two) adds pair
            (key_one, key_two), replacing any pair
            (key_one, other), if any.
        Effects: Mutates self by either replacing a
            pair (key_one, other) with (key_one, key_two),
            or adding a new node with (key_one, key_two)
        add_one: DoubleDict Str Int -> None
        Requires: key_two does not appear as the 
                      second key of any data item in self

        """
        


