from typing import List

class Solution:
    def moveZeros(self, nums: List[int]) -> None:
        i = 0
        j = 0
        while j < len(nums):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i+=1
            j+=1
            
        # while j < len(nums):
        #     if nums[i] == 0 and nums[j] != 0:
        #         nums[i], nums[j] = nums[j], nums[i]
        #         i+=1
        #         j+=1
        #     elif nums[i] != 0 and nums[j] == 0:
        #         i+=1
        #         j+=1
        #     elif nums[i] == 0 and nums[j] == 0:
        #         j+=1
        #     else:
        #         i+=1
        #         j+=1

if __name__ == "__main__":
    nums = [0, 1]
    # nums = [1, 2, 3, 4, 5]
    # nums = [0, 0, 0, 1, 2, 3]
    # nums = [1, 0, 2, 3, 0, 4, 0, 5]
    # nums = [0, 1, 4, 0, 5, 2]
    Solution().moveZeros(nums)
    print(nums)