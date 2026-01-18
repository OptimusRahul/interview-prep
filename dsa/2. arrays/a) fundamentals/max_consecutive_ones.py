from typing import List

class Solution:
    def findMaxConsectivesOnes(self, nums: List[int]) -> int:
        maxCount = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                maxCount = max(maxCount, count)
                count = 0
        return max(maxCount, count)


if __name__ == "__main__":
    nums = [1, 1, 0, 1, 1, 1]
    print(Solution().findMaxConsectivesOnes(nums))