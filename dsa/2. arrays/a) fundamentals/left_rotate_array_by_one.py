from typing import List

class Solution:
    def leftRotateArrayByOne(self, nums: List[int]) -> List[int]:
        temp = nums[0]
        for i in range(1, len(nums)):
            nums[i-1] = nums[i]
        nums[len(nums)-1] = temp
        return nums

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    print(Solution().leftRotateArrayByOne(nums))