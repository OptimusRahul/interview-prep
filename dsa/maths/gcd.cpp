#include <iostream>
using namespace std;

int gcd(int n, int m) {
    int largest = 1;
    for(int i=2; i<=n && i<=m; i++) {
        if(n%i == 0 && m%i == 0) {
            largest = i;
        }
    }
    return largest;
}

int gcd1(int n, int m) {
    if(m == 0) {
        return n;
    }
    return gcd1(m, n%m);
}

int main() {
    int n, m;
    cin >> n >> m;
    cout << gcd(n, m) << endl;
    return 0;
}