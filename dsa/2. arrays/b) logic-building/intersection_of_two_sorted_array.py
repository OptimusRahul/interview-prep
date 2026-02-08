class Solution:
    def intersectionArray(self, nums1, nums2):
        i, j = 0, 0
        intersection = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i+=1
            elif nums1[i] > nums2[j]:
                j+=1
            else:
                intersection.append(nums1[i])
                i+=1
                j+=1
        return intersection
    
if __name__ == "__main__":
    # nums1 = [1, 2, 3, 4, 5]
    # nums2 = [1, 2, 3, 4, 5]

    nums1 = [1, 2, 2, 3, 3, 3]
    nums2 = [2, 3, 3, 4, 5, 7]

    sol = Solution()
    print(sol.intersectionArray(nums1, nums2))