class Solution:
    def kadanesAlgorithm(self, nums):
        maxi = float('-inf')
        sum = 0

        for i in range(len(nums)):
            sum += nums[i]
            if sum > maxi:
                maxi = sum

            if sum < 0:
                sum = 0

        return maxi

if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(Solution().kadanesAlgorithm(nums))