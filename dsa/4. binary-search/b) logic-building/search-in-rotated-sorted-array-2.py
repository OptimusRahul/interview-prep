class Solution:
    def searchInARotatedSortedArrayII(self, nums, k):
        n = len(nums)
        low, high = 0, n - 1
        
        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == k:
                return True

            if nums[low] == nums[mid] == nums[high]:
                low += 1
                high -= 1
                continue

            if nums[low] <= nums[mid]:
                if nums[low] <= k <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= k <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        
        return False

if __name__ == "__main__":
    solution = Solution()
    print(solution.searchInARotatedSortedArrayII([7, 8, 1, 2, 3, 3, 3, 4, 5, 6], 3))
    print(solution.searchInARotatedSortedArrayII([7, 8, 1, 2, 3, 3, 3, 4, 5, 6], 10))
    print(solution.searchInARotatedSortedArrayII([7, 8, 1, 2, 3, 3, 3, 4, 5, 6], 7))