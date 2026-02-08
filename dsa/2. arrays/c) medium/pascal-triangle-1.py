class Solution:
    def nCr(self, n, r):
        if r > n - r:
            r = n - r
        
        if r == 1:
            return n

        res = 1

        for i in range(r):
            res = res * (n - i)
            res = res // (i + 1)

        return res

    def pascalTriangleI(self, r, c):
        return self.nCr(r-1, c-1)

if __name__ == "__main__":
    sol = Solution()
    print(sol.pascalTriangleI(4, 2))
    print(sol.pascalTriangleI(5, 3))