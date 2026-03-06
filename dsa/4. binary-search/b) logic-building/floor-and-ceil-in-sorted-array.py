class Solution:
    def getFloorAndCeil(self, nums, x):
        n = len(nums)
        low, high = 0, n - 1
        floor, ceil = -1, -1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == x:
                floor = nums[mid]
                ceil = nums[mid]

                return [floor, ceil]
            elif nums[mid] < x:
                floor = nums[mid]
                low = mid + 1
            else:
                ceil = nums[mid]
                high = mid - 1

        return [floor, ceil]
       


if __name__ == "__main__":
    solution = Solution()
    print(solution.getFloorAndCeil([3, 4, 4, 7, 8, 10], 5))
    print(solution.getFloorAndCeil([3, 4, 4, 7, 8, 10], 8))
    print(solution.getFloorAndCeil([2, 4, 6, 8, 10, 12, 14], -1))