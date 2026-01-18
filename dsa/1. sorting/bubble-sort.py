from typing import List

class Solution:
    def bubbleSort(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)-i-1):
                if(nums[j] > nums[j+1]):
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return nums
    

if __name__ == "__main__":
    nums = [5, 2, 8, 12, 7]
    print(Solution().bubbleSort(nums))