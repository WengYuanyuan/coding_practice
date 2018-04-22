class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = S.upper().replace('-', '')
        key = ''
        left = len(S)%K
        key += S[:left]
        while left < len(S):
            if len(key) == 0:
                key += S[left:left+K]
            else:
                key += "-" + S[left:left+K]
            left += K
        return key