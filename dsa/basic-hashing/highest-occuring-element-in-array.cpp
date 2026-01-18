#include <bits/stdc++.h>
using namespace std;

int mostFrequentElement(vector<int> &nums)
{
    unordered_map<int, int> map;

    for (int num : nums)
    {
        map[num]++;
    }

    int maxFreq = 0;
    int val = -1;
    for (auto itr : map)
    {
        if (itr.second > maxFreq)
        {
            maxFreq = itr.second;
            val = itr.first;
        }
        else if (itr.second == maxFreq && itr.first < val)
        {
            val = itr.first;
        }
    }

    return val;
}

int main()
{
    int n;
    cin >> n;

    vector<int> nums(n);
    for (int i = 0; i < n; i++)
        cin >> nums[i];

    cout << mostFrequentElement(nums) << endl;

    return 0;
}