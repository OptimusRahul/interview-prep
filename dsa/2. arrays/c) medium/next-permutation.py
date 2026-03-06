from typing import List

class Solution:
    def nextPermutationOptimal(self, nums: List[int]) -> None:
        n = len(nums)
        idx = -1

        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                idx = i
                break

        if idx == -1:
            nums.reverse()
            return

        for i in range(n-1, idx, -1):
            if nums[i] > nums[idx]:
                nums[i], nums[idx] = nums[idx], nums[i]
                break
        nums[idx+1:] = reversed(nums[idx+1:])
        return

    def nextPermutation(self, nums: List[int]) -> None:
        ans = self.getAllPermutations(nums)

        for i in range(len(ans)):
            if list(ans[i]) == nums:
                index = i
                break
        
        nextPerm = ans[0] if index == len(ans) - 1 else ans[index + 1]

        for i in range(len(nextPerm)):
            nums[i] = nextPerm[i]

        return

    def getAllPermutations(self, nums: List[int]) -> List[List[int]]:
        ans: List[List[int]] = []

        self.helperFunc(0, nums, ans)

        ans.sort()
        return ans

    def helperFunc(self, ind, nums: List[int], ans: List[List[int]]) -> None:
        if ind == len(nums):
            ans.append(nums[:])
            return
        
        for i in range(ind, len(nums)):
            nums[ind], nums[i] = nums[i], nums[ind]
            self.helperFunc(ind+1, nums, ans)
            nums[ind], nums[i] = nums[i], nums[ind]

if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3]
    solution.nextPermutationOptimal(nums)
    print(f"Next permutation: {nums}")