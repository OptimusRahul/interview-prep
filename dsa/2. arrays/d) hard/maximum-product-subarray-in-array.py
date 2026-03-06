from typing import List

class Solution:

    def maxProductOptimal(self, nums: List[int]) -> int:
        n = len(nums)
        maxProduct = float('-inf')
        prefix, suffix = 1, 1

        for i in range(n):
            if prefix == 0:
                prefix = 1
            if suffix == 0:
                suffix = 1

            prefix *= nums[i]
            suffix *= nums[n - i - 1]

            maxProduct = max(maxProduct, max(prefix, suffix))

        return int(maxProduct)

    def maxProductBrute(self, nums: List[int]) -> int:
        maxProduct = float('-inf')
        for i in range(len(nums)):
            product = nums[i]
            for j in range(i+1, len(nums)):
                maxProduct = max(maxProduct, product)
                product *= nums[j]

            maxProduct = max(maxProduct, product)
        
        return int(maxProduct)

if __name__ == "__main__":
    sol = Solution()
    nums = [4, 5, 3, 7, 1, 2]
    print(sol.maxProductBrute(nums))
    print(sol.maxProductOptimal(nums))