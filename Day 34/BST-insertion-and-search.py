class TreeNode:
	def __init__(self, value):
		self.val = value
		self.left = None
		self.right = None


class Solution:

	def insert(self, root : TreeNode, value : int) -> TreeNode:
		if root == None:
			return TreeNode(value)

		if root.val > value:
			root.left = self.insert(root.left, value)
		else:
			root.right = self.insert(root.right, value)
		
		return root


	def search(self, root : TreeNode, target : int) -> bool:

		if root == None:
			return False

		if root.val == target:
			return True

		if target > root.val:
			return self.search(root.right, target)
		else:
			return self.search(root.left, target)



			

