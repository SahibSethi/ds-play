def printTree(node):
    if not node:
        return
    printTree(node.left)
    print(node.data)
    printTree(node.right)

def preOrder(node):
	if not node:
		return

	print(node.data)
	preOrder(node.left)
	preOrder(node.right)


def postOrder(node):
	if not node:
		return

	postOrder(node.left)
	postOrder(node.right)
	print(node.data)
