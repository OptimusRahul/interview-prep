from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        right = n - 1
        maxSum, leftSum, rightSum = 0, 0, 0

        for i in range(k):
            leftSum += cardPoints[i]

        maxSum = leftSum

        for i in range(k - 1, -1, -1):
            leftSum -= cardPoints[i]
            rightSum += cardPoints[right]
            maxSum = max(maxSum , leftSum + rightSum)
            right -= 1

        return maxSum

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxScore([1, 2, 3, 4, 5, 6], 3))
