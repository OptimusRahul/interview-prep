class Solution:
    def isPossible(self, nums, pages):
        students = 1
        pagesStudent = 0

        for num in nums:
            if pagesStudent + num <= pages:
                pagesStudent += num
            else:
                students += 1
                pagesStudent = num

        return students

    def findPages(self, nums, m):
        low = max(nums)
        high = sum(nums)

        while low <= high:
            mid = low + (high - low) // 2
            if self.isPossible(nums, mid) <= m:
                high = mid - 1
            else:
                low = mid + 1

        return low

        # for i in range(low, limit + 1):
        #     if self.isPossible(nums, i) <= m:
        #         return i
        # return low

if __name__ == "__main__":
    solution = Solution()
    print(solution.findPages([12, 34, 67, 90], 2))
    print(solution.findPages([25, 46, 28, 49, 24], 4))
    print(solution.findPages([15, 17, 20], 2))