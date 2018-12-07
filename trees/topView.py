from createTree import *
from node import Node
from printTree import *

root = createTree()
root.left.right = Node(6)
root.left.right.right = Node(7)
root.left.right.right.right = Node(8)
root.left.right.right.right.right = Node(9)
printTree(root)


