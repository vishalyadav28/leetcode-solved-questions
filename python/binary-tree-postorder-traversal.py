# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # if root is None:
        #     return []
        # return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
        # O(2n) if we consider reversing the result
        if root is None:
            return []
        stack = [root]
        result = []
        while stack:
            root = stack.pop()
            result.append(root.val)
            if root.left is not None:
                stack.append(root.left)
            
            if root.right is not None:
                stack.append(root.right)
        return result[::-1]

        