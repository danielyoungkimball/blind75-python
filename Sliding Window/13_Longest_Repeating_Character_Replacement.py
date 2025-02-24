# Longest Repeating Character Replacement - Leetcode 424
# https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution(object): 
   class Solution(object):
    def characterReplacement(self, s, k):
        counter = {}
        res = 0

        l = 0
        for r in range(len(s)):
            counter[s[r]] = 1 + counter.get(s[r], 0) # +1 to hash counter otherwise init at 0

            while (r - l + 1) - max(counter.values()) > k:
                # if length of substring minus the most common letter > k replacements
                # then shrink left until valid 
                counter[s[l]] -= 1
                l += 1

            # compare max res to current substring
            # and reiterate
            res = max(res, r - l + 1)
        return res