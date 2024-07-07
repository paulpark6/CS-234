from heighttree import *

# Initialize a height tree and add some nodes
tree = HeightTree()

# Add root node
root = tree.add_leaf(None, "root")

# Test height of root
check.expect("height (root)", tree.height(root), 0)  # Root height should be 0 initially

# Add children
child1 = tree.add_leaf(root, "child1")
child2 = tree.add_leaf(root, "child2")

# Test heights after adding children
check.expect("height (root after adding children)", tree.height(root), 1)
check.expect("height (child1 after adding children)", tree.height(child1), 0)
check.expect("height (child2 after adding children)", tree.height(child2), 0)

# Add a child to child1
child1_1 = tree.add_leaf(child1, "child1_1")

# Test heights after adding a child to child1
check.expect("height (root after adding grandchild)", tree.height(root), 2)
check.expect("height (child1 after adding grandchild)", tree.height(child1), 1)
check.expect("height (child1_1 after adding grandchild)", tree.height(child1_1), 0)

# Add another child to root
child3 = tree.add_leaf(root, "child3")

# Test heights after adding another child to root
check.expect("height (root after adding another child to root)", tree.height(root), 2)
check.expect("height (child3)", tree.height(child3), 0)

# Delete leaf child1_1
tree.delete_leaf(child1_1)

# Test heights after deleting leaf child1_1
check.expect("height (root after deleting leaf child1_1)", tree.height(root), 1)
check.expect("height (child1 after deleting leaf child1_1)", tree.height(child1), 0)

# Delete leaf child3
tree.delete_leaf(child3)

# Test heights after deleting leaf child3
check.expect("height (root after deleting leaf child3)", tree.height(root), 1)
check.expect("height (child2 after deleting leaf child3)", tree.height(child2), 0)

# Add another child to root and delete it
new_child = tree.add_leaf(root, "new_child")
check.expect("height (root after adding new child)", tree.height(root), 1)
tree.delete_leaf(new_child)
check.expect("height (root after deleting new child)", tree.height(root), 1)

# Add and delete a leaf in a deeper tree
child1_2 = tree.add_leaf(child1, "child1_2")
check.expect("height (child1 after adding child1_2)", tree.height(child1), 1)
check.expect("height (root after adding child1_2)", tree.height(root), 2)
tree.delete_leaf(child1_2)
check.expect("height (child1 after deleting child1_2)", tree.height(child1), 0)
check.expect("height (root after deleting child1_2)", tree.height(root), 1)