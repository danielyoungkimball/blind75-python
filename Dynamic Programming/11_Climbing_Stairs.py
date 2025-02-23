# Climbing Stairs - Leetcode 70
# https://leetcode.com/problems/climbing-stairs/description/

class Solution:
    def climbStairs(self, n):
        memo = [0] * (n + 1)
        return self.climb_Stairs(0, n, memo)

    def climb_Stairs(self, current, n, memo):
        if current > n:
            return 0
        if current == n:
            return 1
        if memo[current] > 0:
            return memo[current]
        memo[current] = self.climb_Stairs(current + 1, n, memo) + self.climb_Stairs(current + 2, n, memo)
        return memo[current]