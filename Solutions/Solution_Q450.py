# Solution Provided by Chen Tang (January, 2025)
# LeetCode Question: https://leetcode.com/problems/delete-node-in-a-bst/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            current = root.right

            if not current.left:
                root.val = current.val
                root.right = current.right
            else:
                parent = current
                current = current.left

                while current:
                    if current.left:
                        parent = current
                        current = current.left
                    else:
                        root.val = current.val
                        parent.left = current.right
                        break

        return root