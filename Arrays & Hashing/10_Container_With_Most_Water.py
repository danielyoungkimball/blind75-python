# Container With Most Water - Leetcode 11
# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height):
        """
        Calculate the maximum amount of water a container can store.
        
        :param height: List[int] - List of non-negative integers representing the heights of vertical lines.
        :return: int - Maximum area of water the container can hold.
        """
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            width = right - left
            # Calculate the area bounded by the two lines
            current_area = width * min(height[left], height[right])
            max_area = max(max_area, current_area)

            # Move the pointer corresponding to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area