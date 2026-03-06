class Solution:
    def longestSubarray(self, nums, k):
        n = len(nums)
        maxLen = 0

        for i in range(n):
            currentSum = 0
            for j in range(i, n):
                currentSum += nums[j]

                if currentSum == k:
                    maxLen = max(maxLen, j - i + 1)

        return maxLen

if __name__ == "__main__":
    solution = Solution()
    print(solution.longestSubarray([10, 5, 2, 7, 1, 9], 15))