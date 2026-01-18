#include <iostream>
using namespace std;

/*
*****
*****
*****
*****
*****
*/
void pattern1(int n)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cout << "*";
        }
        cout << endl;
    }
}

/*
 *
 **
 ***
 ****
 *****
 */
void pattern2(int n)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j <= i; j++)
        {
            cout << "*";
        }
        cout << endl;
    }
}

/*
1
12
123
1234
12345
*/
void pattern3(int n)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j <= i; j++)
        {
            cout << j + 1;
        }
        cout << endl;
    }
}

/*
1
22
333
4444
55555
*/
void pattern4(int n)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j <= i; j++)
        {
            cout << i + 1;
        }
        cout << endl;
    }
}

/*
*****
****
***
**
*
*/
void pattern5(int n)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = n; j > i; j--)
        {
            cout << "*";
        }
        cout << endl;
    }
}

/*
12345
1234
123
12
1
*/
void pattern6(int n)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = n, k = 1; j > i; j--, k++)
        {
            cout << k;
        }
        cout << endl;
    }
}

/*
 *
 ***
 *****
 *******
 *********
 */
void pattern7(int n)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = n - 1; j > i; j--)
        {
            cout << " ";
        }

        for (int j = 0; j < (2 * (i + 1)) - 1; j++)
        {
            cout << "*";
        }
        cout << endl;
    }
}

/*
*********
*******
*****
***
*
*/
void pattern8(int n)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < i; j++)
        {
            cout << " ";
        }

        for (int j = (2 * (n - i) - 1); j > 0; j--)
        {
            cout << "*";
        }

        cout << endl;
    }
}

/*
 *
 ***
 *****
 *******
 *********
 *********
 *******
 *****
 ***
 *
 */

void pattern9(int n)
{
    for (int i = 0; i < 2 * n; i++)
    {
        if (i < n)
        {
            for (int j = n - 1; j > i; j--)
            {
                cout << " ";
            }

            for (int j = 0; j < (2 * (i + 1)) - 1; j++)
            {
                cout << "*";
            }
        }
        else
        {
            for (int j = n; j < i; j++)
            {
                cout << " ";
            }
            for (int j = 2 * n - 2 * (i - n) - 1; j > 0; j--)
            {
                cout << "*";
            }
        }

        cout << endl;
    }
}

/*
 *
 **
 ***
 ****
 *****
 ****
 ***
 **
 *
 */
void pattern10(int n)
{
    for (int i = 0; i < 2 * n - 1; i++)
    {
        if (i < n)
        {
            for (int j = 0; j <= i; j++)
            {
                cout << "*";
            }
        }
        else
        {
            for (int j = 2 * n - i - 1; j > 0; j--)
            {
                cout << "*";
            }
        }

        cout << endl;
    }
}

/*
1
0 1
1 0 1
0 1 0 1
1 0 1 0 1
*/
void pattern11(int n)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j <= i; j++)
        {
            if (i % 2 == 0)
            {
                if (j % 2 == 0)
                {
                    cout << "1 ";
                }
                else
                {
                    cout << "0 ";
                }
            }
            else
            {
                if (j % 2 == 0)
                {
                    cout << "0 ";
                }
                else
                {
                    cout << "1 ";
                }
            }
        }
        cout << endl;
    }
}

/*
1        1
12      21
123    321
1234  4321
1234554321
*/
void pattern12(int n)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j <= i; j++)
        {
            cout << j + 1;
        }

        for (int j = 1; j < 2 * (n - i) - 1; j++)
        {
            cout << " ";
        }

        for (int j = i + 1; j > 0; j--)
        {
            cout << j;
        }

        cout << endl;
    }
}

/*
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
*/
void pattern13(int n)
{
    int k = 1;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j <= i; j++)
        {
            cout << k++ << " ";
        }
        cout << endl;
    }
}

/*
A
AB
ABC
ABCD
ABCDE
*/
void pattern14(int n)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j <= i; j++)
        {
            cout << (char)(65 + j);
        }
        cout << endl;
    }
}

/*
ABCDE
ABCD
ABC
AB
A
*/
void pattern15(int n)
{
    for (int i = 0; i < n; i++)
    {
        for (char j = 'A'; j < 'A' + (n - i); j++)
        {
            cout << j;
        }
        cout << endl;
    }
}

/*
A
BB
CCC
DDDD
EEEEE
*/
void pattern16(int n)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j <= i; j++)
        {
            cout << (char)('A' + i);
        }
        cout << endl;
    }
}

/*
    A
   ABA
  ABCBA
 ABCDCBA
ABCDEDCBA
*/
void pattern17(int n)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < (n - i - 1); j++)
        {
            cout << " ";
        }

        for (char ch = 'A'; ch <= 'A' + i; ch++)
        {
            cout << ch;
        }

        for (char ch = 'A' + i - 1; ch >= 'A'; ch--)
        {
            cout << ch;
        }

        cout << endl;
    }
}

/*
E
D E
C D E
B C D E
A B C D E
*/
void pattern18(int n)
{
    for (int i = 0; i < n; i++)
    {
        for (char ch = 'A' + n - i - 1; ch <= 'A' + n - 1; ch++)
        {
            cout << ch << " ";
        }
        cout << endl;
    }
}

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
void pattern19(int n)
{
    for (int i = 0; i < 2 * n; i++)
    {
        if (i < n)
        {
            for (int j = n - i; j > 0; j--)
            {
                cout << "*";
            }

            for (int j = 0; j < 2 * i; j++)
            {
                cout << " ";
            }
            for (int j = n - i; j > 0; j--)
            {
                cout << "*";
            }
        }
        else
        {
            for (int j = 0; j <= (i - n); j++)
            {
                cout << "*";
            }

            for (int j = 0; j < 2 * n - 2 * (i - n) - 2; j++)
            {
                cout << " ";
            }

            for (int j = 0; j <= (i - n); j++)
            {
                cout << "*";
            }
        }

        cout << endl;
    }
}

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
void pattern20(int n)
{
    for (int i = 0; i < 2 * n - 1; i++)
    {
        if (i < n)
        {
            for (int j = 0; j <= i; j++)
            {
                cout << "*";
            }

            for (int j = (2 * (n - i)) - 2; j > 0; j--)
            {
                cout << " ";
            }

            for (int j = 0; j <= i; j++)
            {
                cout << "*";
            }
        }
        else
        {
            for (int j = 2 * n - i - 1; j > 0; j--)
            {
                cout << "*";
            }

            for (int j = 2 * (i - n) + 2; j > 0; j--)
            {
                cout << " ";
            }

            for (int j = 2 * n - i - 1; j > 0; j--)
            {
                cout << "*";
            }
        }

        cout << endl;
    }
}

/*
*****
*   *
*   *
*   *
*****
*/
void pattern21(int n)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (i == 0 || i == n - 1 || j == 0 || j == n - 1)
            {
                cout << "*";
            }
            else
            {
                cout << " ";
            }
        }
        cout << endl;
    }
}

/*
5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 5
5 4 3 3 3 3 3 4 5
5 4 3 2 2 2 3 4 5
5 4 3 2 1 2 3 4 5
5 4 3 2 2 2 3 4 5
5 4 3 3 3 3 3 4 5
5 4 4 4 4 4 4 4 5
5 5 5 5 5 5 5 5 5
*/
void pattern22(int n)
{
    int k = n;
    for (int i = 0; i < 2 * n - 1; i++)
    {
        if (i < n)
        {
            for (int j = 0; j <= i; j++)
            {
                cout << k - j << " ";
            }

            for (int j = 2 * (n - i) - 2; j > 0; j--)
            {
                cout << k - i << " ";
            }

            for (int j = 0; j < i; j++)
            {
                cout << k - i + j + 1 << " ";
            }
        }
        else
        {
            for (int j = 0; j < 2 * n - i - 1; j++)
            {
                cout << k - j << " ";
            }

            for (int j = 0; j < 2 * (i - n); j++)
            {
                cout << "*" << " ";
            }

            // for (int j = 0; j < 2*n-i-1; j++)
            // {
            //     cout << 2*k - i + j << " ";
            // }
        }

        cout << endl;
    }
}

int main()
{
    int n;
    cin >> n;

    pattern22(n);

    return 0;
}