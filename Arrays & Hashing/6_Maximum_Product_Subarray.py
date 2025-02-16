# Maximum Product Subarray - LeetCode 152
# https://leetcode.com/problems/maximum-product-subarray/description/

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_product = nums[0]
        min_product = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < 0:  # Swap max and min when encountering a negative
                max_product, min_product = min_product, max_product

            max_product = max(nums[i], max_product * nums[i])
            min_product = min(nums[i], min_product * nums[i])

            result = max(result, max_product)

        return result
        

          
if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProduct([2,3,-2,4]))  # Output: 6
    print(solution.maxProduct([-2,0,-1])) # Output: 0
