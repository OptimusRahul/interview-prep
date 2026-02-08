from typing import List, Dict

class Solution:
    def twoSumOptimal(self, nums: List[int], target: int) -> List[int]:
        eleIdx = []
        for i in range(len(nums)):
            eleIdx.append([nums[i], i])
        eleIdx.sort()

        left, right = 0, len(nums) - 1

        while left < right:
            sum = eleIdx[left][0] + eleIdx[right][0]

            if(sum == target):
                return [eleIdx[left][1], eleIdx[right][1]]

            if sum > target:
                right -= 1
            else:
                left += 1


        return [-1, -1]

    def twoSumBetter(self, nums: List[int], target: int) -> List[int]:
        numsDict: Dict[int, int] = {}
        for i in range(len(nums)):
            moreNeeded = target - nums[i]
            if moreNeeded in numsDict:
                return [numsDict[moreNeeded], i]
            numsDict[nums[i]] = i
        return [-1, -1]

    def twoSumBrute(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return [-1, -1]


if __name__ == "__main__":
    # nums = [2,7,11,15]
    # target = 9
    nums = [1, 6, 2, 10, 3]
    target = 7
    print(Solution().twoSumBrute(nums, target))
    print(Solution().twoSumBetter(nums, target))
    print(Solution().twoSumOptimal(nums, target))