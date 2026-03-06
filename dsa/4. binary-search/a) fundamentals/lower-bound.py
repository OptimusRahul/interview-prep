class Solution:
    def lowerBound(self, nums, x):
        n = len(nums)
        low, high = 0, n - 1
        idx = n

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] >= x:
                idx = mid
                high = mid - 1
            else:
                low = mid + 1

        return idx

if __name__ == "__main__":
    solution = Solution()
    print(solution.lowerBound([1, 2, 2, 3], 2))
    print(solution.lowerBound([3, 5, 8, 15, 19], 9))
    print(solution.lowerBound([-58210,52968,57654,84387], 89401))