# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob_helper(self, node: Optional[TreeNode]) -> (int, int):
        if not node:
            return (0, 0)

        rob_left, not_rob_left = self.rob_helper(node.left)
        rob_right, not_rob_right = self.rob_helper(node.right)

        rob_node = node.val + not_rob_left + not_rob_right
        not_rob_node = max(rob_left, not_rob_left) + max(rob_right, not_rob_right)

        return (rob_node, not_rob_node)

    def rob(self, root: Optional[TreeNode]) -> int:
        rob_root, not_rob_root = self.rob_helper(root)
        return max(rob_root, not_rob_root)
