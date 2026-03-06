import math
class Solution:
    def sumOfDivisors(self, nums, divisor):
        sum = 0
        for num in nums:
            sum += math.ceil(num / divisor)
        return sum

    def smallestDivisor(self, nums, limit):
        low, high = 1, max(nums)
        while low <= high:
            mid = low + (high - low) // 2
            if self.sumOfDivisors(nums, mid) <= limit:
                high = mid - 1
            else:
                low = mid + 1

        return low

if __name__ == "__main__":
    solution = Solution()
    print(solution.smallestDivisor([7, 15, 6, 3], 8))