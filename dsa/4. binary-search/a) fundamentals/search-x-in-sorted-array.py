class Solution:
    def searchXInSortedArray(self, nums, x):
        n = len(nums)
        low, high = 0, n - 1
        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == x:
                return mid
            elif nums[mid] < x:
                low = mid + 1
            else:
                high = mid - 1


        return -1

if __name__ == "__main__":
    solution = Solution()
    print(solution.searchXInSortedArray([-1,0,3,5,9,12], 9))