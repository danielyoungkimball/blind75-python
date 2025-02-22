# 3Sum - Leetcode 15
# https://leetcode.com/problems/3sum/

from typing import List

class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        n = len(nums)
        result = []

        for i in range(0, n-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i+1
            right = n-1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s < 0:
                    left += 1
                elif s > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    # Skip duplicates for the second element
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicates for the third element
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return result
        
        
class BruteForceSolution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = set()

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                        result.add(triplet)
        return [list(triplet) for triplet in result]

if __name__ == "__main__":
    solution = Solution()
    print(solution.threeSum([-1,0,1,2,-1,-4]))  # Output: [[-1,-1,2],[-1,0,1]]
    bruteForceSolution = BruteForceSolution()
    print(bruteForceSolution.threeSum([0,1,1]))  # Output: []

