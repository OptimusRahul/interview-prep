from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        for i in range(len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]

            if len(res) > 0 and start <= res[-1][1] and end > res[-1][1]:
                res[-1][1] = end
            elif len(res) > 0 and start <= res[-1][1] and end <= res[-1][1]:
                continue
            else:
                res.append([start, end])

        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.merge([[1, 3], [2, 6], [8, 10], [16, 18]]))
    print(solution.merge([[1, 4], [4, 5]]))
    print(solution.merge([[1, 5], [2, 3]]))
    print(solution.merge([[1, 5], [1, 5]]))