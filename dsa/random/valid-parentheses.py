class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in range(len(s)):
            print(stack)
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
            elif len(stack) > 0 and stack[-1] == '(' and s[i] == ')': stack.pop()
            elif len(stack) > 0 and stack[-1] == '{' and s[i] == '}': stack.pop()
            elif len(stack) > 0 and stack[-1] == '[' and s[i] == ']': stack.pop()
            else: stack.append(s[i])

        return len(stack) == 0

if __name__ == "__main__":
    solution = Solution()
    # print(solution.isValid("()"))
    # print(solution.isValid("()[]{}"))
    # print(solution.isValid("(]"))
    # print(solution.isValid("([)]"))
    # print(solution.isValid("{[]}"))
    # print(solution.isValid("([)]"))
    print(solution.isValid("[([]])"))