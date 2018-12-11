from createTree import *
from printTree import *

root = createTree()

def zigzagLevelOrder(root):
    values = []
    queue = [(root, 0)]

    while queue:
        node, depth = queue.pop(0)
        if node:
            if len(values) < depth + 1:
                values.append([])
            if depth % 2:
                values[depth].insert(0, node.data)
            else:
                values[depth].append(node.data)
            queue.append((node.left, depth + 1))
            queue.append((node.right, depth + 1))
    return values

print(zigzagLevelOrder(root))
