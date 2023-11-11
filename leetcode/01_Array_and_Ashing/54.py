# crazy one-line solution
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        height = len(matrix)
        width = len(matrix[0])
        
        top = 0
        bottom = height - 1
        left = 0
        right = width - 1
        
        ans = []
        while top < bottom and left < right:
            for col in range(left, right):
                ans.append(matrix[top][col])
            
            for row in range(top, bottom):
                ans.append(matrix[row][right])
            
            for col in range(right, left, -1):
                ans.append(matrix[bottom][col])
            
            for row in range(bottom, top, -1):
                ans.append(matrix[row][left])
            
            top += 1
            bottom -= 1
            left += 1
            right -= 1
        
        # If a matrix remain inside it is either a 1xn or a mx1
        # a linear scan will return the same order as spiral for these
        if len(ans) < height*width:
            for row in range(top, bottom+1):
                for col in range(left, right+1):
                    ans.append(matrix[row][col])
        
        return ans
