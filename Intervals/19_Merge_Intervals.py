# Merge Intervals – 56
# https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals):
        intervals.sort()  # Sort by start time (O(n log n))
        merged = []
        
        for interval in intervals:
            # If merged is empty or no overlap, add new interval
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # Merge intervals by updating the end time
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged
