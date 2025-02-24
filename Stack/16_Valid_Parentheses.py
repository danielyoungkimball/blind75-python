# Valid Parentheses - 20
# https://leetcode.com/problems/valid-parentheses/description/

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        # ex:
        # ({[]}) valid
        # ((}] invalid
        # (({))} invalid

        # build out all the promises

        stack = []
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                stack.append(s[i])
            else:
                if len(stack) == 0: return False
            
            if s[i] == ")":
                resolution = stack.pop()
                if resolution != "(":
                    return False
            # other brackets
            if s[i] == "}":
                resolution = stack.pop()
                if resolution != "{":
                    return False
            if s[i] == "]":
                resolution = stack.pop()
                if resolution != "[":
                    return False

        return len(stack) == 0