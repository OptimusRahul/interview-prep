from typing import List

class Solution:
    def findRepeatingAndMissingNumber(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sn = n * (n + 1) // 2
        s2n = n * (n + 1) * (2 * n + 1) // 6
        s, s2 = 0, 0

        for i in range(n):
            s += nums[i]
            s2 += nums[i] * nums[i]

        val1 = s - sn
        val2 = s2 - s2n
        val2 = val2 // val1

        x = (val1 + val2) // 2
        y = x - val1

        return sorted([x, y])

if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 6, 7, 5, 7]
    print(sol.findRepeatingAndMissingNumber(nums))  