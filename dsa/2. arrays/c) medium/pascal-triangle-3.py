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

    def generateRow(self, r):
        ansRow = [0] * r
        ansRow[0] = 1
        for i in range(1, r):
            ansRow[i] = (ansRow[i-1] * (r -i)) // i
        return ansRow

    def pascalTriangleIII(self, n):
        ans = []
        for i in range(1, n+1):
            ans.append(self.generateRow(i))
        return ans

    


if __name__ == "__main__":
    sol = Solution()
    print(sol.pascalTriangleIII(4))