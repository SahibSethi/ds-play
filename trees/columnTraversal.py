from createTree import *
from printTree import *

root = createTree()

distanceFromRootMap = {}

def traverseTree(node, d):
	if not node:
		return 
	traverseTree(node.left, d -1)
	distanceFromRootMap.setdefault(d, []).append(node)
	traverseTree(node.right, d+1)


traverseTree(root, 0)
distances = distanceFromRootMap.keys()
distances.sort()

for index in distances:
	for node in distanceFromRootMap[index]:
		print(node.data)
		print('|')
	print('--')

