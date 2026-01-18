#include <bits/stdc++.h>
using namespace std;

int sumOfFirstAndLast(vector<int>& nums) {
    int size = nums.size();
    if(nums.size() == 1) nums[0] + nums[0];
    return nums[0] + nums[size-1];
}

int main() {
    int n;
    cin >> n;

    vector<int> nums(n);

    for(int i=0; i<n; i++) cin >> nums[i];

    cout << sumOfFirstAndLast(nums) << endl;

    return 0;
}