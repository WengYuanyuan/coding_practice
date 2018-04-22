class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        start, end = 0, len(nums)-1
        while end - start > 1:
            mid = (start+end)/2
            if nums[mid] < nums[end]:
                end = mid
            else:
                start = mid
        
        return nums[start] if nums[start] < nums[end] else nums[end]