/*
 *        *
 **      **
 ***    ***
 ****  ****
 **********
 ****  ****
 ***    ***
 **      **
 *        *
 */

#include <iostream>
using namespace std;

void pattern(int n)
{

    for (int i = -(n - 1); i <= (n - 1); i++)
    {
        int row = abs(i);
        for (int j = 0; j < 2 * n; j++)
        {
            if (j <= n - 1 - row || j >= n + row)
                cout << "*";
            else
                cout << " ";
        }
        cout << endl;
    }
    // for (int i = 0; i < n; i++)
    // {
    //     for (int j = 0; j <= i; j++)
    //     {
    //         cout << "*";
    //     }

    //     for (int j = 0; j < 2 * (n - i - 1); j++)
    //     {
    //         cout << " ";
    //     }

    //     for (int j = 0; j <= i; j++)
    //     {
    //         cout << "*";
    //     }

    //     cout << endl;
    // }

    // for (int i = n - 2; i >= 0; i--)
    // {
    //     for (int j = 0; j <= i; j++)
    //     {
    //         cout << "*";
    //     }

    //     for (int j = 0; j < 2 * (n - i - 1); j++)
    //     {
    //         cout << " ";
    //     }
    //     for (int j = 0; j <= i; j++)
    //     {
    //         cout << "*";
    //     }
    //     cout << endl;
    // }
}

int main()
{
    int n;
    cin >> n;

    pattern(n);
}

// int max_space = i < n ? (n - i - 1) * 2 : (i - n + 1) * 2;
// for (int j = 0, k = 0; j < 2 * n; j++)
// {
//     if (j <= i || j < (i - n + 1) * 2)
//         cout << "*";
//     else if (k++ < max_space)
//         cout << " ";
//     else
//         cout << "*";
// }