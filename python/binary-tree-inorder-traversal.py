# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        # if root is None:
        #     return []
        # return self.inorderTraversal(root.left)+[root.val]+self.inorderTraversal(root.right)
        stack = []
        result = []
        while stack != [] or root is not None:
            while root is not None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            result.append(root.val)
            root = root.right
        return result
