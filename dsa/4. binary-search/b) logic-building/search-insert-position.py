class Solution:
    def searchInsertPosition(self, nums, target):
        n = len(nums)
        low, high = 0, n - 1
        idx = n

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                idx = mid + 1
                low = mid + 1
            else:
                idx = mid
                high = mid - 1

        return idx

if __name__ == "__main__":
    solution = Solution()
    print(solution.searchInsertPosition([1, 3, 5, 6], 5))
    print(solution.searchInsertPosition([1, 3, 5, 6], 2))
    print(solution.searchInsertPosition([1, 3, 5, 6], 7))
    print(solution.searchInsertPosition([-4, 4, 6], -5))