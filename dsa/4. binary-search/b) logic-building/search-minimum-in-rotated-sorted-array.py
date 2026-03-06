class Solution:
    def findMin(self, arr):
        n = len(arr)
        low, high = 0, n - 1
        mini = arr[low]

        while low <= high:
            mid = low + (high - low) // 2
            
            if arr[mid] <= mini:
                mini = arr[mid]

            if arr[high] < arr[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return mini

if __name__ == "__main__":  
    solution = Solution()
    print(solution.findMin([4, 5, 6, 7, 0, 1, 2]))
    print(solution.findMin([3, 4, 5, 1, 2]))
    print(solution.findMin([4, 5, 6, 7, -7, 1, 2, 3]))