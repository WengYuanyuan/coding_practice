# -*- coding: utf-8 -*-
class Solution(object):
#big manipulation 
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        max = 1 << len(nums) 
        for i in range (max):
            subset = []
            for j in range(len(nums)):
                if i>>j & 1:
                    subset.append(nums[j])
            result.append(subset)
        return result

        
        
        
        
# # dfs method            
#     def subsets(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         result = []
#         self.dfs(nums, 0, [], result) # 不用sorted(nums)
#         return result
        
#     def dfs(self, nums, index, path, result):
#         result.append(path)
#         for i in xrange(index, len(nums)):
#             self.dfs(nums, i+1, path+[nums[i]],result)


# # dfs method 2
#     def search(self, nums, S, index):
#         if index == len(nums):
#             self.results.append(S)
#             return
        
#         self.search(nums, S + [nums[index]], index + 1)
#         self.search(nums, S, index + 1)
        
#     def subsets(self, nums):
#         self.results = []
#         self.search(sorted(nums), [], 0)
#         return self.results