#include<bits/stdc++.h>
using namespace std;

vector<int> divisors(int n) {
    vector<int> divs;
    for(int i=1; i<=n/2; i++) {
        if(n%i==0) {
            divs.push_back(i);
        }
    }
    return divs;
}

int main() {
    int n;
    cin >> n;


}