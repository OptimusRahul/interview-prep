from typing import Any, List

class Solution:
    def fourSumOptimal(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            for j in range(i+1, n):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                k = j+1
                l = n-1

                while k < l:
                    sum = nums[i] + nums[j] + nums[k] + nums[l]
                    if sum < target:
                        k += 1
                    elif sum > target:
                        l -= 1
                    else:
                        ans.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        l -= 1

                        while k < l and nums[k] == nums[k+1]:
                            k += 1
                        while k < l and nums[l] == nums[l-1]:
                            l -=1 

        return ans


    def fourSumBetter(self, nums: List[int], target: int) -> List[List[int]]:
        ans = set[Any]()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                hashset = set[int]()
                for k in range(j+1, len(nums)):
                    fourth = target - (nums[i] + nums[j] + nums[k])
                    if fourth in hashset:
                        temp = [nums[i], nums[j], nums[k], fourth]
                        temp.sort()
                        ans.add(tuple[int, ...](temp))
                    hashset.add(nums[k])

        return [list(quad) for quad in ans]

    def fourSumBrute(self, nums: List[int], target: int) -> List[List[int]]:
        ans = set[Any]()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    for l in range(k+1, len(nums)):
                        if nums[i] + nums[j] + nums[k] + nums[l] == target:
                            temp = [nums[i], nums[j], nums[k], nums[l]]
                            temp.sort()
                            ans.add(tuple[int, ...](temp))

        return [list(quad) for quad in ans]

if __name__ == "__main__":
    nums =  [1, -2, 3, 5, 7, 9]
    target = 7
    print(Solution().fourSumBrute(nums, target))
    print(Solution().fourSumBetter(nums, target))
    print(Solution().fourSumOptimal(nums, target))