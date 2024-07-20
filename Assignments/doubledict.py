## =======================================================
## Paul Park (20949359)
## CS 234 Spring 2024
## Assignment 4, P1
## =======================================================

#from modules.doubledictnode import *
#import modules.check as check



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
        self._root = None # node storing the root of BST
        self._head = None # node that appears first in ordered linked list


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
        return (self._root is None) and (self._head is None)

    def look_up_one(self, key_one):
        """
        self.look_up_one(key_one) produces the 
            key_two stored with key_one, if any,
            and False otherwise.
        look_up_one: DoubleDict Str 
            -> (anyof Int False)

        """
        node = self._find_bst(self._root,key_one) # look for key_one in BST

        # check if key_one is found or not
        if node is None:
            return False # key_one is not found in BST
        else:
            return node.access_key_two() # gets the pair of key one
        
    def _find_bst(self, root, key_one):
        """
        self._find_bst(root, key_one) produces the node with key_one in BST.
        _find_bst: DoubleDictNode Str 
            -> (anyof DoubleDictNode None)
        """
        if root is None or root.access_key_one() == key_one:
            return root
        elif key_one < root.access_key_one():
            return self._find_bst(root.access_left(), key_one)
        else:
            return self._find_bst(root.access_right(), key_one)
            
    def look_up_two(self, key_two):
        """
        self.look_up_two(key_two) produces the 
            key_one stored with key_two, if any,
            and False otherwise.
        look_up_two: DoubleDict Int 
            -> (anyof Str False)

        """
        node = self._head # get the head of ordered linked list
        while (node is not None): # check if node is empty or not
            if node.access_key_two() == key_two: # check if node has key_two
                return node.access_key_one() # return the pair of key_two
            node = node.access_next() # move to next node
        return False # key_two is not found


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
        new_node = DoubleDictNode(key_one, key_two)
            
        # when BST and linked list are empty
        if self._root is None and self._head is None:
            self._root = new_node
            self._head = new_node
            return
        
        # when BST is not empty
        cnode = self._root  # get the root
        while True:
            cnode_key = cnode.access_key_one()  # get key_one
            
            if key_one < cnode_key:  # go left when key_one is less than current node
                if cnode.access_left() is None:
                    cnode.link_left(new_node)
                    new_node.link_parent(cnode)
                    break
                cnode = cnode.access_left()
            elif key_one > cnode_key:  # go right when key_one is greater than current node
                if cnode.access_right() is None:
                    cnode.link_right(new_node)
                    new_node.link_parent(cnode)
                    break
                cnode = cnode.access_right()
            else:
                cnode.store_key_two(key_two)
                return
        
        # adding key_two to linked list
        cptr = self._head  # get the head
        prev = None
        while cptr is not None and cptr.access_key_two() < key_two:
            prev = cptr
            cptr = cptr.access_next()
        
        new_node.link_next(cptr)
        
        if prev is None:
            self._head = new_node
        else:
            prev.link_next(new_node)
        
    


