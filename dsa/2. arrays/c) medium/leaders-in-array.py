from typing import List

class Solution:
    def leadersInArray1(self, nums: List[int]) -> List[int]:
        leaders = []
        currentLeader = nums[-1]
        leaders.append(currentLeader)

        # Iterate from the second last element to the first
        # This loop iterates over the array from the second last element to the first element, moving right to left.
        # range(len(nums)-2, -1, -1) produces indices starting from len(nums)-2 (second last index) down to 0 (inclusive).
        # For example, for nums = [16, 17, 4, 3, 5, 2], len(nums) = 6, so indices are 4, 3, 2, 1, 0.
        for i in range(len(nums)-2, -1, -1):
            if nums[i] > currentLeader:
                currentLeader = nums[i]
                leaders.append(currentLeader)

        leaders.reverse()

        return leaders

        
    def leadersInArray(self, nums: List[int]) -> List[int]:
        leaders = []
        
        for i in range(len(nums)):
            isLeader = True
            for j in range(i+1, len(nums)):
                if nums[i] <= nums[j]:
                    isLeader = False
                    break
            
            if isLeader:
                leaders.append(nums[i])

        return leaders

if __name__ == "__main__":
    sol = Solution()
    nums = [16, 17, 4, 3, 5, 2]
    # nums2 = [1, 2, 3, 4, 5]
    # nums3 = [5, 4, 3, 2, 1]
    # nums4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # nums5 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    # nums6 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # nums7 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    print(sol.leadersInArray(nums)) # Output: [17, 5, 2]
    # print(sol.leadersInArray(nums2)) # Output: [5]
    # print(sol.leadersInArray(nums3)) # Output: [5]
    # print(sol.leadersInArray(nums4)) # Output: [10]
    # print(sol.leadersInArray(nums5)) # Output: [10]
    # print(sol.leadersInArray(nums6)) # Output: [10]
    # print(sol.leadersInArray(nums7)) # Output: []

    print("--------------------------------")
    print(sol.leadersInArray1(nums)) # Output: [17, 5, 2]
    # print(sol.leadersInArray1(nums2)) # Output: [5]
    # print(sol.leadersInArray1(nums3)) # Output: [5]
    # print(sol.leadersInArray1(nums4)) # Output: [10]
    # print(sol.leadersInArray1(nums5)) # Output: [10]
    # print(sol.leadersInArray1(nums6)) # Output: [10]
    # print(sol.leadersInArray1(nums7)) # Output: []