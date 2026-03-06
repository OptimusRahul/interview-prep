class Solution:
    def subarraySumOptimal(self, nums, k):
        n = len(nums)
        cnt = 0
        prefixSum = 0
        hashmap = {0: 1}

        print(hashmap)

        for i in range(n):
            prefixSum += nums[i]
            moreNeeded = prefixSum - k
            print(f"moreNeeded: {moreNeeded}", hashmap.get(moreNeeded, 0))
            cnt += hashmap.get(moreNeeded, 0)
            hashmap[prefixSum] = hashmap.get(prefixSum, 0) + 1
        
        print(hashmap)

        return cnt

    # brute force approach
    def subarraySum(self, nums, k):
        n = len(nums)
        cnt = 0

        for i in range(n):
            sum = 0
            for j in range(i, n):
                sum += nums[j]
                if sum == k:
                    cnt += 1
        
        return cnt
                

if __name__ == "__main__":
    solution = Solution()
    print(solution.subarraySum([1, 1, 1], 2))
    print(solution.subarraySumOptimal([1, 1, 1], 2))