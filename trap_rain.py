class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height) 
        if n == 0:
            return 0
        l, r = 0, 0
        res = 0
        while r < n:
            if height[l] <= height[r] and l != r:
                marker = height[l]
                while r - l > 1:
                    res += marker - height[l+1]
                    l += 1
                l = r
            r += 1
        stop = l
        l, r = n-1, n-1
        while l >= stop:
            if height[l] >= height[r] and l != r:
                marker = height[r]
                while r - l > 1:
                    res += marker - height[r-1]
                    r -= 1
                r = l
            l -= 1
        
        return res