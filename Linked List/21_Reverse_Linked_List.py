# Reverse Linked List – 206
# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head):
        prev = None
        current = head

        while current:
            next_node = current.next  # Store next node
            current.next = prev       # Reverse the pointer
            prev = current            # Move prev forward
            current = next_node        # Move current forward

        return prev  # New head of the reversed list
