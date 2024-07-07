from modules.treenode import *
from modules.collection import *
import modules.check as check

##
## =======================================================
## Paul Park (20949359)
## CS 234 Spring 2024
## Assignment 3, Problem 1
## =======================================================
##


#from treenode import *
#from collection import *

class HeightTree:
    """
    Fields: _root is the root TreeNode or None if the 
                tree is empty
    """

    def __init__(self):
        """
        HeightTree() produces an empty heighttree.
        Effects: Create a new, empty heighttree. 
        __init__: -> HeightTree

        """
        self.root = None

    def is_empty(self):
        """
        self.is_empty() produces True if the tree is empty
            and False otherwise.
        is_empty: HeightTree -> Bool

        """
        return self.root is None

    def root(self):
        """
        self.root() produces the root of self.
        root: HeightTree -> TreeNode
        Requires: self is not empty

        """

        return self.root

    def value(self, node):
        """        
        self.value(node) produces the value of node.
        value: HeightTree TreeNode -> Any
        Requires: node is a TreeNode in self

        """
        return node.access_value()

    def height(self, node):
        """        
        self.height(node) produces the height of node.
        height: HeightTree TreeNode -> Int
        Requires: node is a TreeNode in self

        """
        return node.access_height()        
    
    def parent(self, node):
        """
        self.parent(node) produces the TreeNode that is the parent
            of node, if any, and otherwise None.
        parent: HeightTree TreeNode -> (anyof TreeNode None)
        Requires: node is a TreeNode in self

        """
        if node.access_prev() is None: # when node is root node
            return None
        # Check if the node is the first child
        if node.access_prev().access_first() == node:
            return node.access_prev()
        # If the node is not the first child
        sibling = node.access_prev()
        while sibling.access_prev() and sibling.access_prev().access_first() != sibling:
            sibling = sibling.access_prev()
        return sibling.access_prev()


    def children(self, node):
        """        
        self.children(node) produces a collection 
            containing the children of node.
        children: HeightTree TreeNode -> Collection
        Requires: node is a TreeNode in self 

        """
        children = Collection()
        child = node.access_first()
        while child is not None:
            children.add(child)
            child = child.access_next()
        return children
        
    def set_value(self, node, new_value):
        """        
        self.set_value(node, new_value) changes the
            value of node to new_value.
        Effects: Mutates self by changing the value
            of node to new_value.
        set_value: HeightTree TreeNode Any -> None
        Requires: node is a TreeNode in self

        """
        node.store_value(new_value)

    def max_child_height(self, node):
        """        
        self.max_child_height(node) produces the maximum
            height of any child of node, or -1 if node has
            no children.
        max_child_height(self, node): HeightTree TreeNode
            -> Int
        Requires: node is a TreeNode in self

        """
        if node.access_first() is None:
            return -1  # No children

        max_height = -1
        child = node.access_first()
        while child is not None:
            child_height = child.access_height()
            if child_height > max_height:
                max_height = child_height
            child = child.access_next()
        
        return max_height


    def update_height(self, node):
        """
        self.update_height(node) updates the height of the given node and all its ancestors.
        Effects: Mutates self as described above.
        update_height(node): HeightTree TreeNode -> None
        Requires: node is a TreeNode in self.
        """
        while node is not None:
            new_height = self.max_child_height(node) + 1
            if new_height == node.access_height():
                break
            node.store_height(new_height)
            node = self.parent(node)  # Use the parent function to traverse up to the parent node

    
    def add_leaf(self, parent, value):
        """        
        self.add_leaf(parent, value) adds a new leaf storing
            value as a child of parent; if parent is None then
            the new node is the root replacing the entire tree
            (if any).
        Effects: Mutates self as described above.
        add_leaf: HeightTree (anyof TreeNode None) Any
            -> TreeNode
        Requires: parent is either None or a TreeNode in self
        """
        new_node = TreeNode(value=value)
        if parent is None:
            self.root = new_node
        else:
            if parent.access_first() is not None:
                new_node.link_next(parent.access_first())
                parent.access_first().link_prev(new_node)
            parent.link_first(new_node)
            new_node.link_prev(parent)
            self.update_height(parent)  # Update the height starting from the parent node
        
        return new_node
    
    def delete_leaf(self, node):
        """        
        self.delete_leaf(node) deletes node from self.
        Effects: Mutates self by deleting node.
        delete_leaf: HeightTree TreeNode -> None
        Requires: node is a leaf in self
        """
        if node.access_first() is not None:
            raise ValueError("The node to be deleted is not a leaf")

        parent = node.access_prev()

        if node == self.root:
            self.root = None  # Deleting the root node
        else:
            # Remove node from its parent's children
            if parent.access_first() == node:
                parent.link_first(node.access_next())
            else:
                sibling = parent.access_first()
                while sibling.access_next() != node:
                    sibling = sibling.access_next()
                sibling.link_next(node.access_next())

            if node.access_next() is not None:
                node.access_next().link_prev(parent)
            
            self.update_height(parent)  # Update the height starting from the parent node


