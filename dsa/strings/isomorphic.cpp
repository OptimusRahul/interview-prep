#include <bits/stdc++.h>
using namespace std;

bool isomorphic(string s, string t)
{
    unordered_map<char, char> m;
    unordered_map<char, char> n;

    for (int i = 0; i < s.length(); i++)
    {
        if(m[s[i]] != '\0' && m[s[i]] != t[i]) {
            return false;
        } else if(n[t[i]] != '\0' && n[t[i]] != s[i]) {
            return false;
        }
        m[s[i]] = t[i];
        n[t[i]] = s[i];

        // cout << m[s[i]] << " = " << t[i] << endl;
        // cout << m[t[i]] << " = " << s[i] << endl;
    }

    return true;
}

int main()
{
    string s, t;
    cin >> s >> t;

    cout << isomorphic(s, t) << endl;
}
