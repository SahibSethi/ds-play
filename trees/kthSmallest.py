from createTree import *
from printTree import *

root = createTree()

class Solution:
  tree_array = []
  def inOrderTraversal(self, node):
      if not node:
          return
      self.inOrderTraversal(node.left)
      self.tree_array.append(node)
      self.inOrderTraversal(node.right)

  def kthsmallest(self, root, k):
      self.inOrderTraversal(root)
      return self.tree_array[k-1].data


value = Solution().kthsmallest(root, 6)
print(value)
printTree(root)
