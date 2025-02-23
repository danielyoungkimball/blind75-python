# Longest Substring - 3
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        Returns the length of the longest substring without repeating characters.
        
        :param s: Input string.
        :return: Length of the longest substring without duplicates.
        """
        char_index = {}  # Dictionary to store the last index of each character.
        max_length = 0
        start = 0  # Left pointer of the current window.

        for i, char in enumerate(s):
            # If the character is found in the current window,
            # move the start pointer to one position after its last occurrence.
            if char in char_index and char_index[char] >= start:
                start = char_index[char] + 1

            # Update the last seen index of the character.
            char_index[char] = i
            # Update the maximum length found so far.
            max_length = max(max_length, i - start + 1)
        
        return max_length