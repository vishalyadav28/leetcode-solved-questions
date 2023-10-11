# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # O(N)
        # if root is None:
        #     return []
        # return [root.val]+self.preorderTraversal(root.left)+self.preorderTraversal(root.right)
        if root is None:
            return []
        stack = [root]
        result = []
        
        while stack:
            root = stack.pop()
            result.append(root.val)
            if root.right is not None:
                stack.append(root.right)
            if root.left is not None:
                stack.append(root.left)
        return result

        