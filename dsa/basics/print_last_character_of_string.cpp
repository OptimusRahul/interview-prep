#include <iostream>
using namespace std;

char lastChar(string &s) {
    return s[s.length() - 1];
}

int main() {
    string s;
    cin >> s;

    cout << lastChar(s) << endl;

    return 0;
}