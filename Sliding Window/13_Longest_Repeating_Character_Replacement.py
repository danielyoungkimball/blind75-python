# Longest Repeating Character Replacement - Leetcode 424
# https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution(object):
    def characterReplacement(self, s, k):
        count = {}
        max_count = 0
        left = 0
        maxLength = 0
        
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            max_count = max(max_count, count[s[right]])
            
            # If window size minus count of most frequent character is greater than k, shrink window
            while (right - left + 1) - max_count > k:
                count[s[left]] -= 1
                left += 1
            
            maxLength = max(maxLength, right - left + 1)
        
        return maxLength