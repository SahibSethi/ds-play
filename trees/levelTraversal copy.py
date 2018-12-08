class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

root = Node(10)


queue = [None, root]
ltr = False
stack = [4, 5]

while (len(queue) != 1):
  temp = queue.pop(0)
  if not temp:
    if !ltr:
      for i in range(len(stack), 0, -1):
        print(stack.pop(i))
    ltr = !ltr
    queue.append(temp)
  else:
    if ltr:
      print(root.data)
    else:
      stack.append(root.left)
      stack.append(root.right)

    queue.append(root.left)
    queue.append(root.right)

queue = [None, 5, 4]
ltr = False
