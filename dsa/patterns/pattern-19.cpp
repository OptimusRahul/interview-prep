/*
**********
****  ****
***    ***
**      **
*        *
*        *
**      **
***    ***
****  ****
**********
*/

#include <iostream>
using namespace std;

void pattern(int n)
{
    for (int i = 0; i < 2 * n; i++)
    {
        int max_space = i < n ? i * 2 : (2 * n - i - 1) * 2;
        for (int j = 0, k = 0; j < 2 * n; j++)
        {
            if (n - j > i || n - j > 2 * n - i - 1)
                cout << "*";
            else if (k++ < max_space)
                cout << " ";
            else
                cout << "*";
        }

        cout << endl;
    }
}

int main()
{
    int n;
    cin >> n;

    pattern(n);
}