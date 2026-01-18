#include <iostream>
using namespace std;

bool isPrime(int n) {
    bool prime = true;
    for(int i = 2; i < n; i++) {
        if(n % i == 0) {
            prime = false;
            break;
        }
    }
    return prime;
}

int primeUptoN(int n) {
    int count = 0;

    for(int i=2; i<n; i++) {
        if(isPrime(i)) {
            count++;
        }
    }
    
    return count;
}

int main() {
    int n;
    cin >> n;
    cout << primeUptoN(n) << endl;
}