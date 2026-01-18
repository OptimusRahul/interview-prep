#include <bits/stdc++.h>
using namespace std;

vector<char> frequencySort(string& s) {
    unordered_map<char, int> charMap;
    unordered_map<int, vector<char>> freqMap;
    vector<char> res;

    for(int i=0; i<s.length(); i++) {
        charMap[s[i]]++;
    }

    for(auto itr: charMap) {
        freqMap[itr.second].push_back(itr.first);
    }

    for(int i=s.length(); i>0; i--) {
        vector<char> resident = freqMap[i];
        sort(resident.begin(), resident.end());
        res.insert(res.end(), resident.begin(), resident.end());
    }

    return res;
}

int main() {
    string s;
    cin >> s;

    vector<char> res = frequencySort(s);
    
    for(int i=0; i<res.size(); i++) {
        cout << res[i] << " ";
    }
    cout << endl;

    return 0;
}