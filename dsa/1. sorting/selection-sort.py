from typing import List

class Solution:
    def selectionSort(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            min_idx = i
            for j in range(i+1, len(nums)):
                if(nums[j] < nums[min_idx]):
                    min_idx = j
            nums[i], nums[min_idx] = nums[min_idx], nums[i]

        return nums
    

if __name__ == "__main__":
    nums = [5, 2, 8, 12, 7]
    print(Solution().selectionSort(nums))