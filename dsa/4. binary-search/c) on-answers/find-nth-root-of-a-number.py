class Solution:
    def power(self, base, exponent, target):
        result = 1
        for _ in range(exponent):
            result *= base
            if result > target:
                return 2
        if result == target:
            return 1
        return 0

    def NthRoot(self, n, m):
        low, high = 1, m
        while low <= high:
            mid = low + (high - low) // 2
            midN = self.power(mid, n, m)

            if midN == 1:
                return mid
            elif midN == 0:
                low = mid + 1
            else:
                high = mid - 1
        
        return -1
    # def power(self, base, exponent):
    #     result = 1
    #     for i in range(exponent):
    #         result *= base
    #     return result

    # def NthRoot(self, n, m):
    #     low, high = 1, m
    #     while low <= high:
    #         mid = low + (high - low) // 2
    #         midN = self.power(mid, n)
            
    #         print(f"mid: {mid}, midN: {midN}")

    #         if midN == m:
    #             return mid
    #         elif midN < m:
    #             low = mid + 1
    #         else:
    #             high = mid - 1
        
    #     return -1

if __name__ == "__main__":
    solution = Solution()
    print(solution.NthRoot(3, 27))
    print(solution.NthRoot(4, 69))
    print(solution.NthRoot(4, 81))