from createTree import *
from printTree import *

root = createTree()

queue = [None, root]
# Storing distance of each node
hd_node = {}
# Storing all nodes at a distance
m = {}
hd_node[root] = 0
m[0] = [root.data]

while(len(queue) != 1):
    temp = queue.pop(0)
    if temp == None:
        queue.append(temp)
    else:
        if temp.left:
            queue.append(temp.left)
            hd_node[temp.left] = hd_node[temp] - 1
            m.setdefault(hd_node[temp.left], []).append(temp.left.data)
        if temp.right:
            queue.append(temp.right)
            hd_node[temp.right] = hd_node[temp] + 1
            m.setdefault(hd_node[temp.right], []).append(temp.right.data)
print(m)

