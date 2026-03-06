from typing import List

class Solution:
    def merge(self, nums: List[int], low: int, mid: int, high: int) -> int:
        count = 0
        temp = []

        left = low
        right = mid + 1

        while left <= mid and right <= high:
            if nums[left] <= nums[right]:
                temp.append(nums[left])
                left += 1
            else:
                temp.append(nums[right])
                count += mid - left + 1
                right += 1
        
        while left <= mid:
            temp.append(nums[left])
            left += 1
        
        while right <= high:
            temp.append(nums[right])
            right += 1
        
        for i in range(low, high + 1):
            nums[i] = temp[i - low]

        return count

    def mergeSort(self, nums: List[int], low: int, high: int) -> int:
        count = 0
        if low >= high:
            return count
        
        mid = (low + high) // 2
        count += self.mergeSort(nums, low, mid)
        count += self.mergeSort(nums, mid+1, high)
        count += self.merge(nums, low, mid, high)

        return count

    def numberOfInversions(self, nums: List[int]) -> int:
        return self.countInversionBrute(nums)

    def countInversionBrute(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0

        for i in range(n):
            for j in range(i+1, n):
                if nums[i] > nums[j]:
                    count += 1
        return count

if __name__ == "__main__":
    sol = Solution()
    nums = [5, 3, 2, 4, 1]
    print(sol.countInversionBrute(nums))
    print(sol.numberOfInversions(nums))