# Contains Duplicate - LeetCode 217
# https://leetcode.com/problems/contains-duplicate/description/

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        seen = {}  # Dictionary to store seen numbers
        for value in nums:
            if value in seen:
                return True  # Duplicate found
            seen[value] = True  # Store number in dictionary
        
        return False
        
        
if __name__ == "__main__":
    solution = Solution()
    print(solution.containsDuplicate([1,2,3,1]))  # Output: true
    print(solution.containsDuplicate([3,3]))  # Output: true
