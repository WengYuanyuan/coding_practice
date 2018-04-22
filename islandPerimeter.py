class Solution(object):
    def islandPerimeter(self, grid):
        """
        http://liqichen.com/daily-leetcode-463-island-perimeter/
        
        :type grid: List[List[int]]
        :rtype: int
        """
        result = 0
        for grid in [grid, map(list, zip(*grid))]:
            for row in grid:
                value = 0
                for g in row:
                    if g != value:
                        value = g
                        result += 1
                if g == 1:
                    result += 1
        return result
        
        
        
        
        
        
    # def islandPerimeter(self, grid):
    #     """
    #     :type grid: List[List[int]]
    #     :rtype: int
    #     """
    #     def equal(x,y):
    #         if x != y:
    #             return 1
    #         else:
    #             return 0
    #     dif = 0
    #     for i in grid + map(list, zip(*grid)):
    #         dif += sum(map(equal, [0] + i, i + [0]))
    #     return dif