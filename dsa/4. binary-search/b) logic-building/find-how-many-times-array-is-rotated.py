# What's wrong with the original logic?
# The original logic attempts to return "high - mid + 1" as the rotation count as soon as it finds nums[mid] > nums[high], 
# which is not correct. The number of rotations in a rotated sorted array is the index of the minimum element.
# We should use binary search to find the index of the minimum element, which represents the number of rotations.

class Solution:
    def findKRotation(self, nums):
        n = len(nums)
        low, high = 0, n - 1

        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        return low  # The index of the minimum element is the number of rotations

if __name__ == "__main__":
    solution = Solution()
    print(solution.findKRotation([4, 5, 6, 7, 0, 1, 2, 3]))  # 4
    print(solution.findKRotation([3, 4, 5, 1, 2]))           # 3
    print(solution.findKRotation([1, 2, 3, 4, 5]))           # 0
    print(solution.findKRotation([4, 5, 1, 2]))              # 2