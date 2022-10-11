class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.psMatrix = [[0]*(len(matrix[0]) + 1) for r in range(len(matrix) + 1)]
        
        for i in range(len(matrix)):
            sum_ = 0
            for j in range(len(matrix[0])):
                sum_ += matrix[i][j] 
                prefixsum = self.psMatrix[i][j + 1] + sum_
                self.psMatrix[i+1][j+1] = prefixsum
                    
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.psMatrix[row2+1][col2+1] - self.psMatrix[row2+1][col1] - self.psMatrix[row1][col2+1] + self.psMatrix[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)