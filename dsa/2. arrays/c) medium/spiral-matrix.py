from typing import List

class Solution:
    def spiralMatrix(self, matrix: List[List[int]]) -> List[int]:
        result = []
        row, col = len(matrix), len(matrix[0])

        top, left, bottom, right = 0, 0, row - 1, col - 1

        while left <= right and top <= bottom:
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1

            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1

            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result



if __name__ == "__main__":
    solution = Solution()
    # matrix = [[1,2,3],[4,5,6],[7,8,9]]
    matrix = [[1],[2],[3],[4],[5]]
    print(solution.spiralMatrix(matrix))