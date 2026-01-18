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

int main() {
    int n;
    cin >> n;
    cout << isPrime(n) << endl;

    return 0;
}