class Solution:
    def longestNonRepeatingSubstring(self, s: str) -> int:
        n = len(s)
        maxLen = 0

        left, right = 0, 0
        hash = [-1] * 256

        while right < n:
            if hash[ord(s[right])] != -1:
                left = max(left, hash[ord(s[right])] + 1)

            currentLen = right - left + 1

            maxLen = max(currentLen, maxLen)
            hash[ord(s[right])] = right

            right += 1

        return maxLen

        
        # for i in range(n):
        #     hash = [0] * 256
        #     for j in range(i, n):
        #         if hash[ord(s[j])] == 1: 
        #             break
        #         hash[ord(s[j])] = 1
        #         maxLen = max(maxLen, j - i + 1)

        # return maxLen

if __name__ == "__main__":
    solution = Solution()
    print(solution.longestNonRepeatingSubstring("abcabcbb"))