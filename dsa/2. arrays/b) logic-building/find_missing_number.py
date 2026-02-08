from typing import List

class Solution:
    def findMissingNumber1(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = n * (n + 1) // 2
        return total_sum - sum(nums)

    def findMissingNumber2(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)

    def findMissingNumber3(self, nums: List[int]) -> int:
        xor1 = 0
        xor2 = 0
        
        print(f"\nStarting XOR approach to find missing number")
        print(f"Array: {nums}")
        print(f"Array length: {len(nums)}")
        print(f"Initial xor1 (expected numbers): {xor1} (binary: {bin(xor1)})")
        print(f"Initial xor2 (actual numbers): {xor2} (binary: {bin(xor2)})")
        print(f"\n{'Iteration':<10} {'i+1':<6} {'nums[i]':<8} {'xor1 (expected)':<30} {'xor2 (actual)':<30}")
        print("="*90)

        for i in range(len(nums)):
            prev_xor1 = xor1
            prev_xor2 = xor2
            
            xor1 = xor1 ^ (i + 1)
            xor2 = xor2 ^ nums[i]
            
            print(f"{i:<10} {i+1:<6} {nums[i]:<8} {prev_xor1:3d} ^ {i+1:2d} = {xor1:3d} ({bin(xor1):<10}) {prev_xor2:3d} ^ {nums[i]:2d} = {xor2:3d} ({bin(xor2):<10})")
        
        print(f"\n{'='*90}")
        print(f"Final xor1 (all expected 1 to n): {xor1} (binary: {bin(xor1)})")
        print(f"Final xor2 (all actual numbers):  {xor2} (binary: {bin(xor2)})")
        print(f"\nFinal XOR: xor1 ^ xor2 = {xor1} ^ {xor2} = {xor1 ^ xor2}")
        print(f"Binary:    {bin(xor1)} ^ {bin(xor2)} = {bin(xor1 ^ xor2)}")
        print(f"\nMissing number: {xor1 ^ xor2}")
        
        return xor1 ^ xor2

if __name__ == "__main__":
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    sol = Solution()
    print(sol.findMissingNumber1(nums))
    print(sol.findMissingNumber2(nums))
    print(sol.findMissingNumber3(nums))