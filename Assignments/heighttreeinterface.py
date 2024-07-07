from modules.treenode import *
from modules.collection import *

##
## =======================================================
## Paul Park (20949359)
## CS 234 Spring 2024
## Assignment 3, Problem 1
## =======================================================
##


# from treenode import *
# from collection import *
# import check


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
        return node.access_prev()

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
            children.add(children,child)
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
        if node.first_child is None: return -1
        child = node.access_first()
        max_height = -1
        while child is not None:
            h =child.access_height()
            if max_height < h:
                max_height = h
            child = child.access_next()
        return max_height

    def update_height(self, operation):
        """
        self.update_height(operation) updates the height of all nodes in height tree. 
            If operation is "add" then root height is increased
            If operation is "delete" then root height is decreased
            for all nodes.
        Effects: Mutuates self as described above. 
        update_height(operation): HeightTree
            -> None
        Requires: HeightTree is not empty, operation is either "add" or "delete", root height is above 0.
        """
        
        if operation == "add":
            change = 1
        elif operation == "delete":
            change = -1
        
        # creating recursive function
        def update_node_height(node):
            """
            update_node_height(node) recursively updates the height of the node and its children.
            Effects: Mutates node and its children by updating their height.
            update_node_height: TreeNode -> None
        
            """
            node.store_height(node.access_height() + change)
            child = node.access_first()
            while child is not None:
                update_node_height(child)
                child = child.access_next()
        
        update_node_height(self.root)

    def add_leaf(self, parent, value):
        """        
        self.add_leaf(parent, value) adds a new leaf storing
            value as a child of parent; if parent is None then
            the new node is the root replacing the entire tree
            (if any).
        Effects: Mutuates self as described above.
        add_leaf: HeightTree (anyof TreeNode None) Any
            -> TreeNode
        Requires: parent is either None or a TreeNode in self
        """
        new_node = TreeNode(value=value, height=0)
        if parent is None:
            self.root = new_node
        else:
            # If there is an existing first child, link it as the next sibling of the new node
            if parent.access_first() is not None:
                new_node.link_next(parent.access_first())
                parent.access_first().link_prev(new_node)
            # Link the new node as the first child of the parent
            parent.link_first(new_node)
            new_node.link_prev(parent)
        self.update_height("add")
        return new_node

def delete_leaf(self, node):
    """        
    self.delete_leaf(node) deletes node from self.
    Effects: Mutates self by deleting node.
    delete_leaf: HeightTree TreeNode -> None
    Requires: node is a leaf in self or it has children
    """
    parent = node.access_prev()
    first_child = node.access_first()

    if node == self.root:
        if first_child is None:
            self.root = None  # No children, simply delete the root
        else:
            self.root = first_child  # Promote the first child to root
            first_child.link_prev(None)
    else:
        if parent.access_first() == node:
            parent.link_first(first_child)
        else:
            sibling = parent.access_first()
            while sibling.access_next() != node:
                sibling = sibling.access_next()
            sibling.link_next(first_child)
        
        if first_child is not None:
            first_child.link_prev(parent)
        
        # Re-link remaining children of the node
        cur = first_child
        while cur is not None and cur.access_next() is not None:
            cur = cur.access_next()
            cur.link_prev(first_child)

    # Update heights after deletion
    self.update_height("delete")



# Initialize a height tree and add some nodes
tree = HeightTree()
root = tree.add_leaf(None, "root")
print(tree.height(root)) 
child1 = tree.add_leaf(root, "child1")
print(tree.height(root)) 
child2 = tree.add_leaf(root, "child2")
print(tree.height(root)) 
delete_leaf(child1)
print(tree.height(root))
child1_1 = tree.add_leaf(child1, "child1_1")

# Print the initial heights
#print(tree.height(root))  # Should be 1
#print(tree.height(child1))  # Should be 0
#print(tree.height(child2))  # Should be 0
#print(tree.height(child1_1))  # Should be 0

# Update heights after adding a new leaf
#tree.add_leaf(child1, "child1_2")

# Print the updated heights
#print(tree.height(root))  # Should be 2
#print(tree.height(child1))  # Should be 1
#print(tree.height(child2))  # Should be 0
#print(tree.height(child1_1))  # Should be 0
