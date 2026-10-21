class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1
        if matrix[l][0] > target:
            return False
        
        while l <= r:
            m = l + (r-l)//2
            if matrix[m][0] == target:
                return True
            elif matrix[m][0] > target:
                r = m-1
            elif matrix[m][0] < target:
                l = m+1

        row = r
        l, r = 0, len(matrix[row])-1
        if matrix[row][-1] < target:
            return False
        
        while l <= r:
            m = l + (r-l)//2
            if matrix[row][m] == target:
                return True
            elif matrix[row][m] > target:
                r = m-1
            elif matrix[row][m] < target:
                l = m+1

        return False

