# Binary Tree Level Order Traversal – 102
# https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        q = deque()
        q.append(root)
        q.append(None)  # Marker for end of level
        ans = []
        curr_level = []

        while q:
            curr_node = q.popleft()
            if curr_node is None:
                ans.append(curr_level)
                curr_level = []
                if not q:
                    break
                else:
                    q.append(None)
            else:
                curr_level.append(curr_node.val)
                if curr_node.left:
                    q.append(curr_node.left)
                if curr_node.right:
                    q.append(curr_node.right)

        return ans
