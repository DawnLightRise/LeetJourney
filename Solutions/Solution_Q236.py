# Solution Provided by Chen Tang (January, 2025)
# LeetCode Question: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self) -> None:
        self.found_lca = False
        self.found_p = False
        self.found_q = False
        self.lca = None

    def lowestCommonAncestor_helper_dfs(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        if root == p or root == q:
            if root == p:
                self.found_p = True
            else:
                self.found_q = True
            
            return root

        left = self.lowestCommonAncestor_helper_dfs(root.left, p, q)
        right = self.lowestCommonAncestor_helper_dfs(root.right, p, q)

        if self.found_lca:
            return self.lca

        if (left and right) or (root == p and self.found_q) or (self.found_p and root == q):
            self.found_lca = True
            self.lca = root
            return self.lca
        elif left and not right:
            return left
        elif not left and right:
            return right
        else:
            return None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.found_lca = False
        self.found_p = False
        self.found_q = False
        self.lca = None

        return self.lowestCommonAncestor_helper_dfs(root, p, q)