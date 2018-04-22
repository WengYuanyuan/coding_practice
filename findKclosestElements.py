class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        if x < arr[0]:
            return arr[:k]
        if x > arr[-1]:
            return arr[-k:]
        
        start, end = self.findTwoPoints(arr, x)
        results = []
        while len(results)<k:
            left_diff = abs(arr[start] - x) 
            right_diff = abs(arr[end] - x) if end < len(arr) else None
            
            if right_diff == None or left_diff <= right_diff:
                results.insert(0,arr[start])
                start -= 1
            elif left_diff > right_diff :
                results.append(arr[end])
                end += 1
        return results
                  
    def findTwoPoints(self, arr, x):
        start, end = 0, len(arr)-1
        while (end - start) > 1:
            mid = (start + end) / 2
            if arr[mid] < x:
                start = mid
            else:
                end = mid
        return start, end