from node import Node

def createTree():
	root = Node(10)
	root.left = Node(5)
	root.right = Node(15)

	root.left.left = Node(2)
	root.left.right = Node(7)
	root.left.right.left = Node(6)

	root.right.left = Node(13)
	root.right.right = Node(17)
	return root
