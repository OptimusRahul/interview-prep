from typing import List

class Solution:
    # def removeDuplicates(self, nums: List[int]) -> int:
    #     s = set()

    #     for num in nums:
    #         s.add(num)

    #     sorted_unique = sorted(s)

    #     for i in range(len(sorted_unique)):
    #         nums[i] = sorted_unique[i]

    #     return len(sorted_unique)

    def removeDuplicates(self, nums: List[int]) -> int:
        i =0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i+=1
                nums[i] = nums[j]
        return i+1

def printArray(nums, n):
    for i in range(n):
        print(nums[i], end=" ")
    print()

if __name__ == "__main__":
    nums = [1, 1, 2, 2, 2, 3, 3]
    
    print("Original Array: ", end="")
    printArray(nums, len(nums))
    
    # Create an instance of the Solution class
    sol = Solution()
    
    # Function call to remove duplicates from array
    k = sol.removeDuplicates(nums)
    
    print("Array after removing the duplicates: ", end="")
    printArray(nums, k)

        