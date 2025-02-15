# Product of Array Except Self - LeetCode 238
# https://leetcode.com/problems/product-of-array-except-self/description/

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [1] * n  # Initialize result array with 1s

        # Compute left products
        left_product = 1
        for i in range(n):
            res[i] = left_product
            left_product *= nums[i]

        # Compute right products and multiply with left products
        right_product = 1
        for i in range(n - 1, -1, -1):  # Loop backwards
            res[i] *= right_product
            right_product *= nums[i]

        return res
        
        
if __name__ == "__main__":
    solution = Solution()
    print(solution.productExceptSelf([1,2,3,4]))  # Output: [24,12,8,6]
    print(solution.productExceptSelf([-1,1,0,-3,3]))  # Output: [0,0,9,0,0]
