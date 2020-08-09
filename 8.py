'''
A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def __repr__(self):
        return str(self.data)
t = Node(0)
t.left = Node(1)
t.right = Node(0)
t.right.left = Node(1)
t.right.right = Node(0)
t.right.left.left = Node(1)
t.right.left.right = Node(1)
def count(tree):
    global total_count
    if not tree:
        return
    if not tree.left and not tree.right:
        total_count += 1
    if tree.left and tree.right and tree.data == tree.left.data and tree.data == tree.right.data:
        total_count += 1
    if tree.left:
        count(tree.left)
    if tree.right:
        count(tree.right)
    return
total_count = 0
count(t)
print(total_count)
