class Solution(object):
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        s_count = [(char, count) for count, char in enumerate(start) if char == "L" or char == "R"]
        e_count = [(char, count) for count, char in enumerate(end) if char == "L" or char == "R"]
        
        if len(s_count) != len(e_count):
            return False
        
        for (char1, count1), (char2, count2) in zip(s_count, e_count):
            if char1 != char2:
                return False
            if char1 == "L" and count1 < count2:
                return False
            if char1 == "R" and count1 > count2:
                return False
       
        return True