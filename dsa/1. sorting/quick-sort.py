from typing import List

class Solution:
    def quickSort(self, nums: List[int]) -> List[int]:
        self.quickSortHelper(nums, 0, len(nums)-1)
        return nums
    
    def quickSortHelper(self, nums: List[int], low: int, high: int) -> None:
        if low >= high:
            return

        partition_idx = self.partition(nums, low, high)
        self.quickSortHelper(nums, low, partition_idx - 1)
        self.quickSortHelper(nums, partition_idx + 1, high)

    def partition(self, nums: List[int], low: int, high: int) -> int:
        pivot = nums[low]
        i = low
        j = high

        while i < j:
            while i <= high-1 and nums[i] <= pivot:
                i+=1

            while j >= low+1 and nums[j] > pivot:
                j-=1
            
            if i<j:
                nums[i], nums[j] = nums[j], nums[i]
        
        nums[low], nums[j] = nums[j], nums[low]

        return j

if __name__ == "__main__":
    nums = [7, 4, 1, 5, 3]
    print(Solution().quickSort(nums))