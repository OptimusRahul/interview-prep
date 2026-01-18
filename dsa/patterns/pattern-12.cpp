#include<iostream>
using namespace std;

void pattern(int n) {
    for(int i=0; i<n; i++) {
        
        for(int j=0; j<=i; j++) {
            cout << (j+1);
        }

        for(int j=0; j<(n*2 - (i+1)*2); j++) {
            cout << "*";
        }

        for(int j=i; j>=0; j--){
            cout << (j+1);
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

