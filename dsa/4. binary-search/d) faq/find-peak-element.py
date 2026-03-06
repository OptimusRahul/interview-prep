class Solution:
    def findPeakElement(self, nums):
        n = len(nums)
        low, high = 0, n - 1

        while low <= high:
            mid = low + (high - low) // 2
            if (mid == 0 or nums[mid-1] < nums[mid]) and (mid == n -1 or nums[mid+1] < nums[mid]):
                return mid
            if mid == 0 or nums[mid-1] < nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return -1
        # for i in range(n):
        #     if (i == 0 or nums[i-1] < nums[i]) and (i == n -1 or nums[i+1] < nums[i]):
        #         return i
        # return -1
        
if __name__ == "__main__":
    solution = Solution()
    print(solution.findPeakElement([1, 2, 3, 4, 5, 6, 7, 8, 5, 1]))
    print(solution.findPeakElement([1, 2, 1, 3, 5, 6, 4]))
    print(solution.findPeakElement([-2, -1, 3, 4, 5]))