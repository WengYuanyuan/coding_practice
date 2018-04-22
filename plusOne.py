class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits[-1] == 9:
            digits[-1] = 0
            for l in range(len(digits)-2,-1,-1):
                if digits[l] != 9:
                    digits[l]+=1 
                    return digits
                else:
                    digits[l] = 0
            digits.insert(0,1)
        else:
            digits[-1] += 1
        
        return digits