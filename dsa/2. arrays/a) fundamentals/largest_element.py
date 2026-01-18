from typing import List

class Solution:
    def largestElement(self, nums: List[int]) -> int:
        maxElement = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > maxElement:
                maxElement = nums[i]
        return maxElement

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    print(Solution().largestElement(nums))