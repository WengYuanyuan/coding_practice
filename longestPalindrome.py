class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        res = 0
        addition = 0
        for char in s:
            if char not in dic:
                dic[char] = 1
            else:
                dic[char] += 1
        for key in dic.keys():
            res += dic[key]/2
            if dic[key]%2 != 0:
                addition = 1    
        return res*2 + addition