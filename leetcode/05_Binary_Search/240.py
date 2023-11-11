class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # start from the top right corner
        # if the target is smaller than the current element, move left
        # if the target is larger than the current element, move down
        # if the target is equal to the current element, return True
        # if the target is not found, return False

        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])
        row, col = 0, n - 1

        while row < m and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1

        return False





        



            
            
                
