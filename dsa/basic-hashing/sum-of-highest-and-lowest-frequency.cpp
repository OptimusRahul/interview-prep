#include<bits/stdc++.h>
using namespace std;

int sumHighestAndLowestFrequency(vector<int>& nums) {
    unordered_map<int, int> map;

    for(int num: nums) {
        map[num]++;
    }

    if(map.empty()) return -1;

    set<int> s;
    
    for(auto& itr: map) {
        s.insert(itr.second);
    }

    if(s.size() == 1) return *s.begin() * 2;

    int minFreq = *s.begin();
    int maxFreq = *s.rbegin();

    return minFreq + maxFreq;
}

int main() {
    int n;
    cin >> n;

    vector<int> nums(n);
    for(int i=0; i<n; i++) cin >> nums[i];
    
    cout << sumHighestAndLowestFrequency(nums) << endl;

    return 0;
}

