# Permutation in String – 567
# https://leetcode.com/problems/permutation-in-string/

class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False
            
        # hashmap1 for s1 character counts
        char_count_1 = {}
        for char in s1:
            char_count_1[char] = char_count_1.get(char, 0) + 1
        
        # hashmap2 for the sliding window in s2
        char_count_2 = {}
        for i in range(len(s1)):
            char = s2[i]
            char_count_2[char] = char_count_2.get(char, 0) + 1

        if char_count_1 == char_count_2:
            return True

        # sliding window over s2
        for i in range(len(s2) - len(s1)):  
            j = i + len(s1)

            char_to_rm = s2[i]  # Character leaving the window
            char_to_add = s2[j]  # Character entering the window

            # Add new character
            char_count_2[char_to_add] = char_count_2.get(char_to_add, 0) + 1

            # Remove old character
            char_count_2[char_to_rm] -= 1
            if char_count_2[char_to_rm] == 0:
                del char_count_2[char_to_rm]  # Only delete if count is 0

            # Check if maps match
            if char_count_1 == char_count_2:
                return True

        return False