#include <iostream>
using namespace std;

int LCM(int g1, int g2) {
    int max = g1 > g2 ? g1 : g2;
    for(int i = 1; i<=max; i++) {
        int multiple = i * max;
        if(multiple % g1 == 0 && multiple % g2 == 0) {
            return multiple;
        }
    }
    return -1;
}

int gcd1(int n, int m) {
    if(m == 0) {
        return n;
    }
    return gcd1(m, n%m);
}

int lcm1(int n, int m) {
    return n*m/gcd1(n, m);
}

int main() {
    int n, m;
    cin >> n >> m;
    cout << LCM(n, m) << endl;
    cout << lcm1(n, m) << endl;
}