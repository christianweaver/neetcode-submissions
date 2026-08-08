class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        T = 0
        B = len(matrix) - 1

        M_row = None
        while T <= B:
            M_row = T + ((B - T) // 2)
            if matrix[M_row][0] == target:
                return True
            elif matrix[M_row][0] < target:
                T = M_row + 1
            else:
                B = M_row - 1
        
        if matrix[M_row][0] > target:
            M_row -= 1
        
        L = 0
        R = len(matrix[M_row]) - 1

        while L <= R:
            M = L + ((R - L) // 2)
            if matrix[M_row][M] == target:
                return True
            elif matrix[M_row][M] < target:
                L = M + 1
            else:
                R = M - 1
        
        return False
