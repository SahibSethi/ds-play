from node import Node

root = Node(10)
l_node = Node(5)
r_node = Node(15)
root.left = l_node
root.right = r_node

root.left.left = Node(2)
root.left.right = Node(7)
root.left.right.left = Node(6)

root.right.left = Node(13)
root.right.right = Node(17)

def traverse(node):
	if not node.left and not node.right:
		return True
	if node.left:
		isLeaf = traverse(node.left)
		if isLeaf:
			node.left = None
	if node.right:
		isLeaf = traverse(node.right)
		if isLeaf:
			node.right = None
	return False


def printTree(node):
	if not node:
		return
	printTree(node.left)
	print(node.data)
	printTree(node.right)

printTree(root)
print('-----')
traverse(root)
print('-----')
printTree(root)
