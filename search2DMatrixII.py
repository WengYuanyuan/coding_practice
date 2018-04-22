class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False
        if len(matrix[0]) == 0:
            return False
        m, n = len(matrix), len(matrix[0])
        r, c = 0, n-1
        while r < m and c>=0:
            if matrix[r][c] == target:
                return True
            if matrix[r][c] < target:
                r += 1
            else:
                c -= 1
        return False