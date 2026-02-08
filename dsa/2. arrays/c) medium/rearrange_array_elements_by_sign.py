from typing import List

class Solution:
    def rearrangeArrayElementsBySign2(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        posIdx, negIdx = 0, 1
        for num in nums:
            if num > 0:
                ans[posIdx] = num
                posIdx += 2
            else:
                ans[negIdx] = num
                negIdx += 2
        return ans

    def rearrangeArrayElementsBySign(self, nums: List[int]) -> List[int]:
        pos, neg, result = [], [], []

        for num in nums:
            if num > 0:
                pos.append(num)
            else:
                neg.append(num)

        for i in range(len(pos)):
            result.append(pos[i])
            result.append(neg[i])
        return result

if __name__ == "__main__":
    sol = Solution()
    nums = [3, -2, -1, 4, 5, -6, -7, 8]
    print(sol.rearrangeArrayElementsBySign(nums))
    print(sol.rearrangeArrayElementsBySign2(nums))