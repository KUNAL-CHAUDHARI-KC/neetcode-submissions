class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
       rows = len(matrix)
       columns = len(matrix[0])

       l = 0
       r = (rows * columns) - 1

       while l <= r:
            mid = (l+r) // 2
            row = mid // columns
            col = mid % columns

            if matrix[row][col] > target:
                r = mid-1

            elif matrix[row][col] < target:
                l = mid+1
            
            else:
                return True
        
       return False