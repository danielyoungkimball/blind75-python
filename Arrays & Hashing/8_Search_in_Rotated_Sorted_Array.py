# Search in Rotated Sorted Array - Leetcode 33
# https://leetcode.com/problems/search-in-rotated-sorted-array/

from typing import List

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2  # Compute mid index
            if nums[mid] == target:
                return mid  # Found target, return index
            
            # Determine if the left half is sorted
            if nums[left] <= nums[mid]:
                # Check if target is in the left sorted half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # Otherwise, right half is sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1  # Target not found

        

if __name__ == "__main__":
    solution = Solution()
    print(solution.search([4,5,6,7,0,1,2], 0))  # Output: 4
