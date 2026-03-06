from typing import List
from collections import defaultdict

class Solution:
    def majorityElementIIOptimal(self, nums: List[int]) -> List[int]:
        n = len(nums)
        cnt1, cnt2 = 0, 0
        ele1, ele2 = float('-inf'), float('-inf')

        for i in range(n):
            if cnt1 == 0 and ele2 != nums[i]:
                cnt1 = 1
                ele1 = nums[i]
            elif cnt2 == 0 and ele1 != nums[i]:
                cnt2 = 1
                ele2 = nums[i]
            elif ele1 == nums[i]:
                cnt1 += 1
            elif ele2 == nums[i]:
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1

        cnt1, cnt2 = 0, 0

        for num in nums:
            if num == ele1:
                cnt1 += 1
            elif num == ele2:
                cnt2 += 1

        mini = n // 3 + 1
        result = []

        if cnt1 >= mini:
            result.append(ele1)
        if cnt2 >= mini and ele2 != ele1:
            result.append(ele2)

        return result





    def majorityElementIIBetter(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        mini = n // 3 + 1
        # defaultdict is a subclass of dict that returns a default value if the key has not been set yet.
        # Here, defaultdict(int) means that any new key accessed will automatically default to 0.
        map = defaultdict(int)

        for i in range(n):
            map[nums[i]] += 1

            if map[nums[i]] == mini:
                result.append(nums[i])

            if len(result) == 2:
                break

        return result
    
    def majorityElementIIBrute(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []

        for i in range(n):
            if len(result) == 0 or result[0] != nums[i]:
                count = 0
                
                for j in range(n):
                    if nums[j] == nums[i]:
                        count += 1

                if count > n // 3:
                    result.append(nums[i])

            if len(result) == 2:
                break

        return result

    def majorityElementII(self, nums: List[int]) -> List[int]:
        # Time complexity: O(n^2) because for each unique element (at most n), nums.count(num) takes O(n) time.
        return [num for num in set(nums) if nums.count(num) > len(nums) // 3]

if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 1, 1, 3, 2]
    print(sol.majorityElementII(nums))
    print(sol.majorityElementIIBrute(nums))
    print(sol.majorityElementIIBetter(nums))
    print(sol.majorityElementIIOptimal(nums))