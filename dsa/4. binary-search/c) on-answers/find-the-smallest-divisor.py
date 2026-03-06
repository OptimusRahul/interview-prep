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
    # def smallestDivisor(self, nums, limit):
    #     maxEle = max(nums)
    #     for d in range(1, maxEle):
    #         sum = 0
    #         for num in nums:
    #             sum += math.ceil(num / d)

    #         if sum <= limit:
    #             return d
    #     return -1

if __name__ == "__main__":
    solution = Solution()
    print(solution.smallestDivisor([1, 2, 3, 4, 5], 8))
    print(solution.smallestDivisor([8, 4, 2, 3], 6))
    print(solution.smallestDivisor([8, 4, 2, 3], 4))
    print(solution.smallestDivisor([8, 4, 2, 3], 8))