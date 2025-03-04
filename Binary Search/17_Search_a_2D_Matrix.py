# Search a 2D Matrix – 74
# https://leetcode.com/problems/search-a-2d-matrix/

class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False  # Edge case for empty matrix

        row, col = len(matrix) - 1, 0  # Start from bottom-left
        while row >= 0 and col < len(matrix[0]):
            current = matrix[row][col]

            if current == target:
                return True
            elif current < target:
                col += 1  # Move right
            else:
                row -= 1  # Move up

        return False
