#include<bits/stdc++.h>
using namespace std;

void whichWeekDay(int n) {
    switch(n) {
        case 1: cout << "Monday" << endl; break;
        case 2: cout << "Tuesday" << endl; break;
        case 3: cout << "Wednessday" << endl; break;
        case 4: cout << "Thursday" << endl; break;
        case 5: cout << "Friday" << endl; break;
        case 6: cout << "Saturday" << endl; break;
        case 7: cout << "Sunday" << endl; break;
        default: cout << "Invalid" << endl;
    }
}

int main() {
    int n;
    cin >> n;
    whichWeekDay(n);
    return 0;
}