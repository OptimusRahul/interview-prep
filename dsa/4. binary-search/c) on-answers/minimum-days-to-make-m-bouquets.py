class Solution:
    def isPossible(self, nums, day, k, m):
        bouquets, flowers = 0, 0

        for num in nums:
            if num <= day:
                flowers += 1
            else:
                bouquets += (flowers // k)
                flowers = 0

        bouquets += (flowers // k)
        return bouquets >= m

    # def roseGarden(self, n, nums, k, m):
    #     if k * m > n:
    #         return -1

    #     low, high = min(nums), max(nums)

    #     for num in range(low, high + 1):
    #         if self.isPossible(nums, num, k, m):
    #             return num
    #     return -1

    def roseGarden(self, n, nums, k, m):
        if k * m > n:
            return -1

        low, high = min(nums), max(nums)

        while low <= high:
            mid = low + (high - low) // 2
            if self.isPossible(nums, mid, k, m):
                high = mid -1
            else:
                low = mid + 1

        return low

        # for num in range(low, high + 1):
        #     if self.isPossible(nums, num, k, m):
        #         return num
        # return -1

if __name__ == "__main__":
    solution = Solution()
    print(solution.roseGarden(8, [7, 7, 7, 7, 13, 11, 12, 7], 2, 3))
    print(solution.roseGarden(5, [1, 10, 3, 10, 2], 3, 2))
    print(solution.roseGarden(5, [1, 10, 3, 10, 2], 1, 3))