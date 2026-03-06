from typing import List

class Solution:
    def mergeOptimal(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j = m - 1, n - 1
        idx = m + n - 1

        while j >= 0:
            if i >= 0 and nums1[i] >= nums2[j]:
                nums1[idx] = nums1[i]
                idx -= 1
                i -= 1
            else:
                nums1[idx] = nums2[j]
                idx -= 1
                j -= 1
        
    def swapIfGreater(self, nums1: List[int], nums2: List[int], left: int, right: int) -> None:
        if nums1[left] > nums2[right]:
            nums1[left], nums2[right] = nums2[right], nums1[left]

    def mergeGap(self, nums1: List[int], nums2: List[int]) -> None:
        m, n = len(nums1), len(nums2)
        length = m + n
        gap = (length // 2) + (length % 2)

        while gap > 0:
            left = 0
            right = left + gap

            while right < length:
                if left < m and right >= m:
                    self.swapIfGreater(nums1, nums2, left, right - m)
                elif left  >= m:
                    self.swapIfGreater(nums2, nums2, left - m, right - m)
                else:
                    self.swapIfGreater(nums1, nums1, left, right)
                
                left += 1
                right += 1

            if gap == 1:
                break

            gap = (gap // 2) + (gap % 2)

    def merge(self, nums1: List[int], nums2: List[int]) -> None:
        n, m = len(nums1), len(nums2)
        i, j = n - 1, 0
        while i >= 0 and j < m:
            if nums1[i] > nums2[j]:
                nums1[i], nums2[j] = nums2[j], nums1[i]
                i -= 1
                j += 1
            else:
                break
        nums1.sort()
        nums2.sort()

if __name__ == "__main__":
    sol = Solution()

    nums1 = [1, 3, 5, 7]
    nums2 = [2, 4, 6, 8]
    sol.merge(nums1, nums2)
    print("merge:", nums1, nums2)

    nums1 = [1, 3, 5, 7]
    nums2 = [2, 4, 6, 8]
    sol.mergeGap(nums1, nums2)
    print("mergeGap:", nums1, nums2)

    nums1 = [1, 3, 5, 7, 0, 0, 0, 0]
    nums2 = [2, 4, 6, 8]
    sol.mergeOptimal(nums1, 4, nums2, 4)
    print("mergeOptimal:", nums1)