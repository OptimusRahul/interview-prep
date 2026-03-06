class Solution:

    # optimal approach
    def subarrayXorOptimal(self, nums, k):
        n = len(nums)
        cnt = 0
        prefixXor = 0
        hashmap = {0: 1}

        for i in range(n):
            prefixXor ^= nums[i]
            moreNeeded = prefixXor ^ k
            cnt += hashmap.get(moreNeeded, 0)
            hashmap[prefixXor] = hashmap.get(prefixXor, 0) + 1

        return cnt

    # brute force approach
    def subarrayXor(self, nums, k):
        n = len(nums)
        cnt = 0

        for i in range(n):
            xor = 0
            for j in range(i, n):
                xor ^= nums[j]
                if xor == k:
                    cnt += 1

        return cnt


if __name__ == "__main__":
    solution = Solution()
    print(solution.subarrayXor([4, 2, 2, 6, 4], 6))