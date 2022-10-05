class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        opening = "({["
        closing = ")}]"
        for ch in s:
            if ch in opening:
                stack.append(ch)
            elif ch in closing:
                if len(stack) == 0:
                    return False
                elif opening.find(stack.pop()) != closing.find(ch):
                    return False
                
        return len(stack) == 0