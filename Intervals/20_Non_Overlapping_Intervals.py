# Non Overlapping Intervals – 435
# https://leetcode.com/problems/non-overlapping-intervals/

class Solution:
    def eraseOverlapIntervals(self, intervals):
        if not intervals:
            return 0
        
        # Step 1: Sort by end time (Greedy)
        intervals.sort(key=lambda x: x[1])  # Sort by end times

        # Step 2: Use a greedy approach to count removals
        end = float('-inf')  # Stores the end time of the last added interval
        counter = 0

        for interval in intervals:
            start, finish = interval
            # If there's an overlap (start < last stored end time), remove this interval
            if start < end:
                counter += 1  # Count this interval for removal
            else:
                end = finish  # Update the last stored end time
            
            print(counter, finish)

        return counter
