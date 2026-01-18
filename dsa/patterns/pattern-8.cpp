/*

*********
1*******
12*****
123***
1234*

*/

#include <bits/stdc++.h>
using namespace std;

void pattern(int n) {
    for(int i=1; i<=n; i++) {
        for(int j=1; j<i; j++){
            cout << " ";
        }

        for(int j=1; j<=((2*n)-(i*2)+1); j++){
            cout << "*";
        }

        cout << endl;
    }
}

int main() {
    int n;
    cin >> n;

    pattern(n);

    return 0;
}
