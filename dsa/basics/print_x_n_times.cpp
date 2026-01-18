#include <iostream>
using namespace std;

void printX(int X, int N)
{
    while (N) {
        if (N == 1) {
            cout << X;
        } else {
            cout << X << " ";
        }
        N--;
    }
    cout << endl;
    return;
}

int main()
{
    int x, n;
    cin >> x >> n;
    printX(x, n);
    
}