class Solution:
    def singleNonDuplicate(self, nums):
        n = len(nums)
        if n == 1:
            return nums[0]
            
        if nums[0] != nums[1]:
           return nums[0]

        if nums[n - 1] != nums[n - 2]:
            return nums[n - 1]
           
        low, high = 1, n - 2

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] != nums[mid + 1] and nums[mid] != nums[mid - 1]:
                return nums[mid]

            if mid % 2 == 1 and nums[mid] == nums[mid - 1] or mid % 2 == 0 and nums[mid] == nums[mid + 1]:
                low = mid + 1
            else:
                high = mid - 1
        
        return -1

if __name__ == "__main__":
    solution = Solution()
    print(solution.singleNonDuplicate([1, 1, 2, 2, 3, 3, 4, 4, 5]))
    print(solution.singleNonDuplicate([1, 1, 3, 5, 5]))
    print(solution.singleNonDuplicate([1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]))
    print(solution.singleNonDuplicate([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7]))