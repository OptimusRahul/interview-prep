from typing import List

class Solution:
    def reverse(self, nums: List[int], start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    def leftRotateByKPlaces(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, len(nums)-1)
        self.reverse(nums, 0, len(nums)-1)

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    k = 2
    Solution().leftRotateByKPlaces(nums, k)
    print(nums)