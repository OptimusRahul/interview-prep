#include <iostream>
using namespace std;

int _calsum(int n, int pow) {
    int sum=1;
    while(pow--) {
        cout << n << " " << pow << " " << n << endl;
        sum*=n;
    }
    cout << "sum " << sum << endl;
    
    return sum;
}

bool isArmstrong(int n) {
    int _n = n, __n = n;
    int count = 0;
    int sum = 0;

    while(_n) {
        count++;
        _n/=10;
    }

    while(n) {
        int digit = n%10;
        sum += _calsum(digit, count);
        n/=10;
    }

    return sum == __n;
}

int main() {
    int n;
    cin >> n;
    cout << isArmstrong(n);

    return 0;
}
