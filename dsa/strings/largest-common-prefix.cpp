#include<bits/stdc++.h>
using namespace std;

string longestCommonPrefix(vector<string>& str) {
    string res = "";
    for(int i=0; i<str[0].length(); i++) {
        char ch = str[0][i];
        for(int j=1; j<str.size(); j++){
            if(i>str[j].length() || str[j][i] != ch){
                return res;
            }
        }
        res += ch;
    }

    return res;
}

int main() {
    int n;
    cin >> n;

    vector<string> str(n);

    for(int i=0; i<n; i++) cin >> str[i];

    cout << longestCommonPrefix(str) << endl;

    return 0;
}

