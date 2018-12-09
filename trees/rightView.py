from createTree import *


root = createTree()

max_level = [0]

def recursive(node, level, max_level):
	if not node:
		return
	if level > max_level[0]:
		max_level[0] = level
		print(node.data)

	recursive(node.right, level + 1, max_level)
	recursive(node.left, level + 1, max_level)

recursive(root, 1, max_level)


