# Merge Two Sorted Lists – 21
# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        # Edge cases: If one list is empty, return the other
        if not list1:
            return list2
        if not list2:
            return list1
        
        # Determine the starting node (smaller head)
        min_head = list1 if list1.val < list2.val else list2
        current = min_head

        # Move list1 or list2 forward depending on which was chosen as head
        if min_head == list1:
            list1 = list1.next
        else:
            list2 = list2.next
        
        # Merging process
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            
            current = current.next  # Move forward
        
        # Attach remaining elements if any
        current.next = list1 if list1 else list2

        return min_head
