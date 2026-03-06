class Solution:
    # def longestConsecutive(self, nums):
    #     nums.sort()
    #     cnt, maxLen = 1, 1
    #     for i in range(1, len(nums)):
    #         if nums[i] == nums[i-1]:
    #             continue
    #         elif nums[i] == nums[i-1] + 1:
    #             cnt += 1
    #         else:
    #             maxLen = max(maxLen, cnt)
    #             cnt = 1

    #     return maxLen

    def longestConsecutive(self, nums):
        n = len(nums)
        if n == 0:
            return 0

        longest = 1
        st = set(nums)

        for i in range(n):
            st.add(nums[i])

        print(st)

        for num in st:
            print(f"num: {num}", num - 1 not in st)
            if num - 1 not in st:
                print(f"num: {num} is a starting point")
                cnt = 1
                current = num

                while current + 1 in st:
                    current += 1
                    cnt += 1
                
                longest = max(longest, cnt)

        return longest
                


        
if __name__ == "__main__":
    solution = Solution()
    print(solution.longestConsecutive([100, 4, 200, 1, 3, 2]))