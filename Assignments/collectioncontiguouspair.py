from modules.contiguous import *
from modules.pair import *
import modules.check as check

INFINITY = 100

class Collection:
    """
    Fields: _first contains the index of the first empty slot
            _contents contains Pairs, each with a data item 
                and a count of the number of copies
    """

    def __init__(self):
        """
        Collection() produces a new, empty collection.
        Effects: Creates a new, empty collection.        
        __init__: -> Collection

        """
        self.array = Contiguous(INFINITY)
        self.size = 0

    def __repr__(self):
        """
        repr(self) produces a string representation of the data stored in the collection.
        __repr__: Collection -> Str
        """
        to_return = ""
        for index in range(self.size):  # Loop through the filled slots
            current_pair = self.array.access(index)  # Access each Pair in the array
            current_data = current_pair.pair_first()  # Get the data item
            current_count = current_pair.pair_second()  # Get the count of the item
            to_return += f"[{current_data}, {current_count}] "  # Append to the result string
        return to_return.strip()  # Remove any trailing whitespace


    def is_empty(self):
        """
        self.is_empty() produces True if self is empty and
            False otherwise.
        value: Collection -> Bool
 
        """

        return self.size == 0
    
        

    def add(self, item):
        """
        self.add(item) adds item to self.
        Effects: Adds item to self
        add: Collection Any -> None
        """
        # when adding the first Pair to Array
        if self.size == 0:
            self.array.store(0, Pair(item, 1))
            self.size += 1
            return None

        # Check if the item already exists in the collection
        for i in range(self.size):
            if self.array.access(i).pair_first() == item:
                second = self.array.access(i).pair_second()
                self.array.store(i, Pair(item, second + 1))
                return None

        # When adding a new pair to the array (size > 0)
        if self.size < self.array.size():  # Ensure size does not exceed the limit
            self.array.store(self.size, Pair(item, 1))
            self.size += 1

    def delete_any(self):
        """
        self.delete_any() produces an item and removes it from self.
        Effects: Removes an item from self
        delete_any: Collection -> Any
        Requires: self is nonempty

        """
        # QUESTION: what are we returning? Pair(item, previous # of copies) or just Item or Pair(item, new # of copies after removal) -> will do just item for now

        # Ensure the collection is nonempty
        if self.size <= 0:
            return None

        # Access the last element in the collection
        remove = self.array.access(self.size - 1)

        # Case 1: Removing an element with multiple copies (no need to change size)
        if remove.pair_second() > 1:
            self.array.store(self.size - 1, Pair(remove.pair_first(), remove.pair_second() - 1))
            return remove.pair_first()
        else:
            # Case 2: Removing the last copy of the element (change size of the array)
            self.size -= 1
            return remove.pair_first()
        
                

######### testing code test 1 #############

# Create a new collection instance
coll = Collection()

# Test 1: Add an item to the empty collection
coll.add('apple')
check.expect("Add Test 1", coll.array.access(0).pair_first(), 'apple')
check.expect("Add Test 1 (count)", coll.array.access(0).pair_second(), 1)

# Test 2: Add another of the same item
coll.add('apple')
check.expect("Add Test 2", coll.array.access(0).pair_first(), 'apple')
check.expect("Add Test 2 (count)", coll.array.access(0).pair_second(), 2)

# Test 3: Add a different item
coll.add('banana')
check.expect("Add Test 3", coll.array.access(1).pair_first(), 'banana')
check.expect("Add Test 3 (count)", coll.array.access(1).pair_second(), 1)

# Test 4: Add another different item
coll.add('cherry')
check.expect("Add Test 4", coll.array.access(2).pair_first(), 'cherry')
check.expect("Add Test 4 (count)", coll.array.access(2).pair_second(), 1)

# Test 5: Delete an item from the collection (last full slot)
deleted_item = coll.delete_any()
check.expect("Delete Test 1", deleted_item, 'cherry')
check.expect("Delete Test 1 (size)", coll.size, 2)

# Test 6: Delete another item (multiple copies)
deleted_item = coll.delete_any()
check.expect("Delete Test 2", deleted_item, 'banana')
check.expect("Delete Test 2 (size)", coll.size, 1)

# Test 7: Delete another item (multiple copies)
deleted_item = coll.delete_any()
check.expect("Delete Test 3", deleted_item, 'apple')
check.expect("Delete Test 3 (count)", coll.array.access(0).pair_second(), 1)
check.expect("Delete Test 3 (size)", coll.size, 1)

# Test 8: Delete the last item
deleted_item = coll.delete_any()
check.expect("Delete Test 4", deleted_item, 'apple')
check.expect("Delete Test 4 (size)", coll.size, 0)


