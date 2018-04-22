class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        match = {")":"(", "}":"{", "]":"["}
        stack = []
        for char in s:
            if char in match.keys():
                if stack == [] or match[char]!= stack.pop():
                    return False
                # else:
                #     stack.pop()
            else: 
                stack.append(char)
        return stack == []