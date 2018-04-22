class Solution(object):
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        m = len(image)
        n = len(image[0])
        if m == 0 or n == 0:
            return 0
        
        upper = x
        lower = m - 1
        while upper < lower :
            mid = (upper + lower) / 2 + 1
            if '1' in image[mid]:
                upper = mid 
            else:
                lower = mid - 1
        bottom = upper
        
        upper = 0
        lower = x
        while upper < lower:
            mid = (upper + lower) / 2 
            if '1' not in image[mid]:
                upper = mid + 1
            else:
                lower = mid
        top = lower
        
        image = map (list, zip(*image))
        upper = y
        lower = n - 1
        while upper < lower :
            mid = (upper + lower) / 2 + 1
            if '1' in image[mid]:
                upper = mid 
            else:
                lower = mid - 1
        right = upper
        
        upper = 0
        lower = y
        while upper < lower:
            mid = (upper + lower) / 2 
            if '1' not in image[mid]:
                upper = mid + 1
            else:
                lower = mid
        left = lower
        
        return (bottom - top + 1) * (right - left + 1)