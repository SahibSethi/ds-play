def printTree(node):
    if not node:
        return
    printTree(node.left)
    print(node.data)
    printTree(node.right)
