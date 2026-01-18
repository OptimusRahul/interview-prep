#include <bits/stdc++.h>
using namespace std;

int secondMostFrequentElement(vector<int>& nums) {
    unordered_map<int, int> map;
    int maxFreq = -1, secondMaxFreq = -1;

    for(auto itr: nums) {
        map[itr]++;
        if(map[itr] > maxFreq) {
            maxFreq = map[itr];
        }
    }

    int val = -1;
    for(auto itr: map) {
        if(itr.second > secondMaxFreq && itr.second != maxFreq) {
            secondMaxFreq = itr.second;
            val = itr.first;
        } else if(itr.second == secondMaxFreq && itr.second != maxFreq) {
            val = min(val, itr.first);
        }
    }
    
    return val;
}

int main() {
    int n;
    cin >> n;

    vector<int> nums(n);

    for(int i=0; i<n; i++) cin >> nums[i];

    cout << secondMostFrequentElement(nums) << endl;

    return 0;
}
