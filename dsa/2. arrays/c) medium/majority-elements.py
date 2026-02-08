class Solution:
    def majorityElement4(self, nums):
        n = len(nums)
        count, ele = 0, 0

        for i in range(n):
            if count == 0:
                ele = nums[i]
                count = 1
            elif nums[i] == ele:
                count += 1
            else:
                count -= 1

        print(f"Majority element: {ele}")

        cnt1 = nums.count(ele)
        if cnt1 > n // 2:
            return ele
        
        return -1
        
    def majorityElement3(self, nums):
        if len(nums) == 1:
            return nums[0]

        nums.sort()

        return nums[len(nums) // 2]

    def majorityElement2(self, nums):
        if len(nums) == 1:
            return nums[0]

        numsDict = {}

        for num in nums:
            numsDict[num] = numsDict.get(num, 0) + 1

        for num, count in numsDict.items():
            if count > len(nums) // 2:
                return num
            
        return -1

    def majorityElement1(self, nums):
        if len(nums) == 1:
            return nums[0]

        nums.sort()

        # print(f"Sorted nums: {nums}")

        currElement, currCount = nums[0], 1
        maxElement, maxCount = currElement, currCount
        for i in range(1, len(nums)):
            if currElement == nums[i]:
                currCount += 1
            elif currCount > maxCount:
                maxElement, maxCount = currElement, currCount
                currElement, currCount = nums[i], 1
            else:
                currElement, currCount = nums[i], 1
        
        if currCount > maxCount:
            maxElement, maxCount = currElement, currCount

        return maxElement



    def majorityElement(self, nums):
        if len(nums) == 1:
            return nums[0]
        
        maxElement = None
        maxCount = 0

        for i in range(0, len(nums)):
            currElement = nums[i]
            currCount = 1
            for j in range(i+1, len(nums)):
                if currElement == nums[j]:
                    currCount += 1
            if currCount > maxCount:
                maxCount = currCount
                maxElement = currElement

        return maxElement

if __name__ == "__main__":
    nums = [2, 2, 1, 1, 1, 2, 2]
    nums2 = [3, 2, 3]
    nums3 = [1]
    nums4 = [7,1,7,2,7,3,7,4,7,5,7,6,7]

    sol = Solution()
    
    print(sol.majorityElement(nums)) # Output: 2
    print(sol.majorityElement(nums2)) # Output: 3
    print(sol.majorityElement(nums3)) # Output: 1
    print(sol.majorityElement(nums4)) # Output: 7

    print("--------------------------------")
    print(sol.majorityElement1(nums)) # Output: 2
    print(sol.majorityElement1(nums2)) # Output: 3
    print(sol.majorityElement1(nums3)) # Output: 1
    print(sol.majorityElement1(nums4)) # Output: 7

    print("--------------------------------")
    print(sol.majorityElement2(nums)) # Output: 2
    print(sol.majorityElement2(nums2)) # Output: 3
    print(sol.majorityElement2(nums3)) # Output: 1
    print(sol.majorityElement2(nums4)) # Output: 7

    print("--------------------------------")
    print(sol.majorityElement3(nums)) # Output: 2
    print(sol.majorityElement3(nums2)) # Output: 3
    print(sol.majorityElement3(nums3)) # Output: 1
    print(sol.majorityElement3(nums4)) # Output: 7

    print("--------------------------------")
    print(sol.majorityElement4(nums)) # Output: 2
    print(sol.majorityElement4(nums2)) # Output: 3
    print(sol.majorityElement4(nums3)) # Output: 1
    print(sol.majorityElement4(nums4)) # Output: 7