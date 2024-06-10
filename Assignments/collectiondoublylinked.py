##
## =======================================================
## Paul Park (20949359)
## CS 234 Spring 2024
## Assignment 2, Problem 2
## =======================================================
##

#from modules.contiguous import *
#from modules.linked import *
#import modules.check as check


from linked import *
from contiguous import *
import check

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
        self.head = None
        self.tail = None
        

    def __repr__(self):
        """
        repr(self) produces a string of the data stored.
        __repr__: Collection -> Str

        """
        current = self.head
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
        return self.head is None


    def add(self, item):
        """
        self.add(item) adds item to self.
        Effects: Adds item to self
        add: Collection Any -> None

        """
        # create a new Node with item
        new_node = Double(item)

        # case 1: adding to empty collection
        # create new Doubly linked set head to this new node, set tail to this new node
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            return

        # case 2: adding to non empty collection
        # original first item (store a temp value of it)
        tmp = self.head
        # set new head pointer to new ndoe
        self.head.link_prev(new_node)
        # change the head to new node
        self.head = new_node
        # make sure new node is also pointing to previous head value
        new_node.link_next(tmp)
        return
    
    def delete_any(self):
        """
        self.delete_any() produces an item and removes it from self.
        Effects: Removes an item from self
        delete_any: Collection -> Any
        Requires: self is nonempty

        """
        current_head = self.head # nothing in collection
        if (self.head == self.tail): # Case 1: Only one item in collection
            self.head = None
            self.tail = None
        else:
            next_head = current_head.next() # Case 2: More than one item in collection
            # remove current head, make sure current self.head is not pointing to anything.
            self.head.link_next(None)
            self.head.link_prev(None)
            # new head
            self.head = next_head
            # make sure no connection to previous head
            next_head.link_prev(None)
        return current_head.access()
    
                
clist = Collection()
    
# Test initial empty list
check.expect("Test 1: Initial list is empty", clist.is_empty(), True)

# Test adding elements
clist.add(10)
clist.add(20)
clist.add(30)
check.expect("Test 2: List after adding 30, 20, 10", [clist.head.access(), clist.head.next().access(), clist.head.next().next().access()], [30, 20, 10])
print(clist)
# Test deleting elements
deleted_item = clist.delete_any()
check.expect("Test 3: Deleted item is 30", deleted_item, 30)
check.expect("Test 4: List after deleting 30", [clist.head.access(), clist.head.next().access()], [20, 10])

deleted_item = clist.delete_any()
check.expect("Test 5: Deleted item is 20", deleted_item, 20)
check.expect("Test 6: List after deleting 20", [clist.head.access()], [10])

deleted_item = clist.delete_any()
check.expect("Test 7: Deleted item is 10", deleted_item, 10)
check.expect("Test 8: List is empty after deleting all items", clist.is_empty(), True)

