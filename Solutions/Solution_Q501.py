# Solution Provided by Chen Tang (January, 2025)
# LeetCode Question: https://leetcode.com/problems/find-mode-in-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.prev_val = None
        self.counts = 1
        self.max_count = 1
        self.results = []

    def in_order(self, node: Optional[TreeNode]) -> None:
        if not node:
            return

        self.in_order(node.left)

        if self.prev_val is not None:
            if node.val == self.prev_val:
                self.counts += 1
            else:
                self.counts = 1

        if self.counts > self.max_count:
            self.results = [node.val]
            self.max_count = self.counts
        elif self.counts == self.max_count:
            self.results.append(node.val)

        self.prev_val = node.val

        self.in_order(node.right)

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.prev_val = None
        self.counts = 1
        self.max_count = 1
        self.results = []

        self.in_order(root)
        
        return self.results