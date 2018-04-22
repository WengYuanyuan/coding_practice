class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1,-1]
        
        start, end = 0, len(nums)-1       
        while end - start > 1:
            mid = (start + end) / 2
            if nums[mid] >= target:
                end = mid
            else:
                start = mid
        if nums[start] == target:
            left = start
        elif nums[end] == target:
            left = end
        else:
            return [-1,-1]
        
        start, end = 0, len(nums)-1       
        while end - start > 1:
            mid = (start + end) / 2
            if nums[mid] > target:
                end = mid
            else:
                start = mid
        if nums[end] == target:
            right = end
        elif nums[start] == target:
            right = start
        
        return [left, right]