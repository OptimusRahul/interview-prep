class Solution:
    def search(self, nums, target):
        n = len(nums)
        low, high = 0, n - 1
        
        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                return mid
            
            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1

if __name__ == "__main__":
    solution = Solution()
    print(solution.search([4, 5, 6, 7, 0, 1, 2], 0))
    print(solution.search([4, 5, 6, 7, 0, 1, 2], 3))
    print(solution.search([4, 5, 6, 7, 0, 1, 2], 5))
    print(solution.search([39,45,48,52,74,-82,-81,-77,-74,-70,-46,-37,-29,-28,-15,15,19,27,33], 52))
