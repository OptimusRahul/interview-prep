class Solution:
    def lowerBound(self, nums, x):
        n = len(nums)
        low, high = 0, n - 1
        first = -1

        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == x:
                first = mid
                high = mid - 1
            elif nums[mid] < x:
                low = mid + 1
            else:
                high = mid - 1

        return first

    def upperBound(self, nums, x):
        n = len(nums)
        low, high = 0, n - 1
        last = -1

        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == x:
                last = mid
                low = mid + 1
            elif nums[mid] < x:
                low = mid + 1
            else:
                high = mid - 1

        return last
        
    def searchRange(self, nums, x):
        first = self.lowerBound(nums, x)
        if first == -1:
            return [-1, -1]
        last = self.upperBound(nums, x)
        return [first, last]

if __name__ == "__main__":
    solution = Solution()
    print(solution.searchRange([5, 7, 7, 8, 8, 10], 8))
    print(solution.searchRange([5, 7, 7, 8, 8, 10], 6))
    print(solution.searchRange([5, 7, 7, 8, 8, 10], 5))