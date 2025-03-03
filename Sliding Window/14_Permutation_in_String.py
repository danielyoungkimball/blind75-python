# Permutation in String – 567
# https://leetcode.com/problems/permutation-in-string/

from collections import Counter

class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False  # If s1 is longer, it can't be a substring

        s1_count = Counter(s1)
        window_count = Counter(s2[:len(s1)])  # Initialize window

        if s1_count == window_count:
            return True  # First window matches

        for i in range(len(s1), len(s2)):
            start_char = s2[i - len(s1)]  # Character leaving the window
            new_char = s2[i]  # New character entering the window

            # Remove old character
            window_count[start_char] -= 1
            if window_count[start_char] == 0:
                del window_count[start_char]  # Remove if count hits 0

            # Add new character
            window_count[new_char] += 1

            # Check if current window matches s1
            if window_count == s1_count:
                return True

        return False
