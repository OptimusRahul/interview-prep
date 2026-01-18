from typing import List

class Solution:
    def mergeSort(self, nums: List[int]) -> List[int]:
        self.mergeSortHelper(nums, 0, len(nums)-1)
        return nums

    def mergeSortHelper(self, nums: List[int], low: int, high: int) -> None:
        if low >= high:
            return
        # (low + high) / 2 does floating point division and results in a float,
        # while (low + high) // 2 does integer division and returns an integer (which is required for list indexing).
        mid = (low + high) // 2
        self.mergeSortHelper(nums, low, mid)
        self.mergeSortHelper(nums, mid+1, high)
        self.merge(nums, low, mid, high)

    def merge(self, nums: List[int], low: int, mid: int, high: int) -> None:
        temp = []
        left = low
        right = mid + 1

        while left <= mid and right <= high:
            if nums[left] <= nums[right]:
                temp.append(nums[left])
                left += 1
            else:
                temp.append(nums[right])
                right += 1

        while left <= mid:
            temp.append(nums[left])
            left += 1
        
        while right <= high:
            temp.append(nums[right])
            right += 1

        for i in range(len(temp)):
            nums[low + i] = temp[i]

if __name__ == "__main__":
    nums = [7, 4, 1, 5, 3]
    print(Solution().mergeSort(nums))