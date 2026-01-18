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

#include <iostream>
using namespace std;

void pattern(int n)
{
    int loop = 2 * n - 1;
    int half = loop / 2;
    for (int i = 0; i < loop; i++)
    {
        for (int j = 0; j < loop; j++)
        {
            cout << max(abs(i - half), abs(j - half)) + 1 << " ";
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