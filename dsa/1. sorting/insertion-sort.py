from typing import List

class Solution:
    def insertionSort(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            key = nums[i]
            j = i-1
            while j>= 0 and nums[j] > key:
                nums[j+1] = nums[j]
                j-=1
            nums[j+1] = key
        return nums

if __name__ == "__main__":
    nums = [5, 2, 8, 12, 7]
    print(Solution().insertionSort(nums))