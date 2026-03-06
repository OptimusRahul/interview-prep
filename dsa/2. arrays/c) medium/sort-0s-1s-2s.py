from typing import List

class Solution:
    def sort012Optimal(self, nums: List[int]) -> List[int]:
        low, mid, high = 0, 0, len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
        return nums

    def sort012OBetter(self, nums: List[int]) -> List[int]:
        count0, count1, count2 = 0, 0, 0
        for num in nums:
            if num == 0:
                count0 += 1
            elif num == 1:
                count1 += 1
            else:
                count2 += 1
        return [0] * count0 + [1] * count1 + [2] * count2

    def sort012Brute(self, nums: List[int]) -> List[int]:
        nums.sort()
        return nums

if __name__ == "__main__":
    solution = Solution()
    nums = [0, 1, 2, 0, 1, 2]
    nums1 = solution.sort012Brute(nums)
    nums2 = solution.sort012OBetter(nums)
    nums3 = solution.sort012Optimal(nums)
    print(f"Sorted array: {nums1}")
    print(f"Sorted array: {nums2}")
    print(f"Sorted array: {nums3}")