#include <bits/stdc++.h>
using namespace std;

int longestConsecutiveSequence(vector<int> &nums)
{
    unordered_set<int> s;
    for (int num : nums)
    {
        s.insert(num);
    }
    int longest = 0;
    for (auto itr : s)
    {
        cout << "num: " << itr << " " << s.count(itr - 1) << endl;
        if (s.find(itr - 1) == s.end())
        {
            int currentNum = itr;
            longest++;
        }
    }
    return longest;
}

int main()
{
    int n;
    cin >> n;
    vector<int> nums(n);
    for (int i = 0; i < n; i++)
        cin >> nums[i];
    cout << longestConsecutiveSequence(nums) << endl;
    return 0;
}