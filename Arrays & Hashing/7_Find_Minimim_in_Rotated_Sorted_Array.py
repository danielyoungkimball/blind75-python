# Find Minimum in Rotated Sorted Array - LeetCode 153
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:  # Minimum is in the right half
                left = mid + 1
            else:  # Minimum is in the left half or is mid itself
                right = mid

        return nums[left]  # `left` now points to the minimum