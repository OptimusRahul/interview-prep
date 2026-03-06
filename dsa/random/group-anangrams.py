from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [[strs[0]]]

        mpp: dict[str, list[str]] = {}

        for i in range(len(strs)):
            key = strs[i]
            key = "".join(sorted(list(key)))

            mpp[key] = mpp.get(key, []) + [strs[i]]

        res = []
        for key in mpp:
            res.append(mpp[key])

        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))