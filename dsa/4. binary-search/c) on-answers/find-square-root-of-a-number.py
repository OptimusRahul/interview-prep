class Solution:
    def floorSqrt(self, n: int) -> int:
        low, high = 1, n + 1

        while low <= high:
            mid = low + (high - low) // 2
            val = mid * mid

            if val <= n:
                low = mid + 1
            else:
                high = mid - 1

        return high

if __name__ == "__main__":
    solution = Solution()
    print(solution.floorSqrt(36))
    print(solution.floorSqrt(28))
    print(solution.floorSqrt(50))