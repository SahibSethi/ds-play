from createTree import *
from printTree import *

root = createTree()

queue = [None, root]

while(len(queue) != 1):
	temp = queue.pop(0)
	if temp == None:
		queue.append(temp)
		print('------')
	else:
		print(temp.data)
		if temp.left:
			queue.append(temp.left)
		if temp.right:
			queue.append(temp.right)

