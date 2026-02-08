from typing import List

class Solution:
    def threeSumOptimal(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = n -1

            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum < 0:
                    j += 1
                elif sum > 0:
                    k -= 1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]: 
                        j += 1
                    while j < k and nums[k] == nums[k-1]: 
                        k -= 1

        return ans

    def threeSumBetter(self, nums: List[int]) -> List[List[int]]:
        triplets = set()

        for i in range(len(nums)):
            hashset = set()
            for j in range(i+1, len(nums)):
                third = -(nums[i] + nums[j])
                if third in hashset:
                    temp = [nums[i], nums[j], third]
                    temp.sort()
                    triplets.add(tuple(temp))
                hashset.add(nums[j])

        ans = [list(triplet) for triplet in triplets]
        return ans
    
    def threeSumBrute(self, nums: List[int]) -> List[List[int]]:
        triplets = set()

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        temp = [nums[i], nums[j], nums[k]]
                        temp.sort()
                        triplets.add(tuple(temp))

        ans = [list(triplet) for triplet in triplets]
        return ans

if __name__ == "__main__":
    # nums = [-1,0,1,2,-1,-4]
    nums = [2,-2,0,3,-3,5]
    import time

    sol = Solution()

    start = time.time()
    print("Brute Force Output:", sol.threeSumBrute(nums))
    print("Brute Force Time: {:.6f} seconds".format(time.time() - start))

    start = time.time()
    print("Better Output:", sol.threeSumBetter(nums))
    print("Better Time: {:.6f} seconds".format(time.time() - start))

    start = time.time()
    print("Optimal Output:", sol.threeSumOptimal(nums))
    print("Optimal Time: {:.6f} seconds".format(time.time() - start))