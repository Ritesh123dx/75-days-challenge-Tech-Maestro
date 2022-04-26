class TreeNode:
	def __init__(self, value):
		self.val = value
		self.left = None
		self.right = None


class Solution:

	def findMax(self, root):
		while root.right !=  None:
			root = root.right

		return root.val


	def deleteNode(self, root : TreeNode, target : int) -> TreeNode:
		if root == None:
			return None

		if root.val > target:
			root.left = self.deleteNode(root.left, target)
			return root
		elif root.val < target:
			root.right = self.deleteNode(root.right, target)
			return root

		if root.left == None and root.right == None:
			del root
			return None

		elif root.left == None or root.right == None:
			child_node = root.left if root.left != None else root.right

			del root
			return child_node

		else:
			inorder_predecessor_value = self.FindMax(root.left)
			self.deleteNode(root.left, inorder_predecessor_value)

			root.val = inorder_predecessor_value

			return root


