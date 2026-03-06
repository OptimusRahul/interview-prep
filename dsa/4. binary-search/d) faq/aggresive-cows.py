class Solution:
    def isPossible(self, nums, distance, k):
        cnt = 1
        lastPlaced = nums[0]

        for i in range(1, len(nums)):
            if nums[i] - lastPlaced >= distance:
                cnt += 1
                lastPlaced = nums[i]
            if cnt >= k:
                return True

        return False


    def aggressiveCows(self, nums, k):
        nums.sort()
        low, high = 1, nums[-1] - nums[0]
        while low <= high:
            mid = low + (high - low) // 2
            if self.isPossible(nums, mid, k):
                low = mid + 1
            else:
                high = mid - 1
        
        return high

        # limit = nums[-1] - nums[0]
        # for i in range(1, limit + 1):
        #     if not self.isPossible(nums, i, k):
        #         return i - 1

        # return limit

if __name__ == "__main__":
    solution = Solution()
    print(solution.aggressiveCows([0, 3, 4, 7, 10, 9], 4))
    print(solution.aggressiveCows([4, 2, 1, 3, 6], 2))
    print(solution.aggressiveCows([10, 1, 2, 7, 5], 3))