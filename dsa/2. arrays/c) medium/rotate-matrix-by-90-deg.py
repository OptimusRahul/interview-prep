from typing import List

class Solution:
    def displayMatrix(self, matrix: List[List[int]]) -> None:
        for row in matrix:
            print(row)

    def rotateMatrix(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
        for i in range(n):
            matrix[i].reverse()

if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Solution().displayMatrix(matrix)
    Solution().rotateMatrix(matrix)
    Solution().displayMatrix(matrix)