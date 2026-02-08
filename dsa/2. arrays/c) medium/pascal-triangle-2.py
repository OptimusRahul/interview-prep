class Solution:
    def nCr(self, n, r):
        if r > n-r:
            r = n-r
        
        if r == 1:
            return n

        res = 1

        for i in range(r):
            res = res * (n - i)
            res = res // (i + 1)

        return res

    def pascalTriangleII(self, r):
        ans = [0] * r
        ans[0] = 1
        for i in range(1, r):
            # ans.append(self.nCr(r-1, i-1))
            ans[i] = (ans[i-1] * (r -i)) // i

        return ans

    


if __name__ == "__main__":
    sol = Solution()
    print(sol.pascalTriangleII(4))