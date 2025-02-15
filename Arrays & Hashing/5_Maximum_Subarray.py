# Maximum Subarray - LeetCode 53
# https://leetcode.com/problems/maximum-subarray/description/

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]  # Initialize with the first element
        current_sum = nums[0]

        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])  # Choose to start a new subarray or extend the current one
            max_sum = max(max_sum, current_sum)  # Update max sum if current is larger

        return max_sum
        
        
if __name__ == "__main__":
    solution = Solution()
    print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # Output: 6
    print(solution.maxSubArray([1])) # Output: 1
    print(solution.maxSubArray([5,4,-1,7,8]))  # Output: 23
