from typing import List

class Solution:
    def secondLargestElement(self, nums: List[int]) -> int:
        maxElement = nums[0]
        secondMaxElement = None
        for i in range(1, len(nums)):
            if nums[i] > maxElement:
                secondMaxElement = maxElement
                maxElement = nums[i]
            elif nums[i] != maxElement and (secondMaxElement is None or nums[i] > secondMaxElement):
                secondMaxElement = nums[i]
        return -1 if secondMaxElement is None else secondMaxElement

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    print(Solution().secondLargestElement(nums))