#include <bits/stdc++.h>
using namespace std;

string largeOddNum(string &s)
{
    int lastOddIndex = -1;

    for (int i = s.length() - 1; i >= 0; i--)
    {
        int digit = s[i] - '0';
        if (digit % 2 != 0)
        {
            lastOddIndex = i;
            break;
        }
    }

    if (lastOddIndex == -1)
    {
        return "";
    }

    int start = 0;
    while (start < lastOddIndex && s[start] == '0')
    {
        start++;
    }

    return s.substr(start, lastOddIndex - start + 1);
}

string largestOddNum(string &s)
{
    int num = stoi(s);

    int largestOdd = -1;

    while (num)
    {
        int digit = num % 10;
        if (digit % 2 != 0)
        {
            largestOdd = num;
            break;
        }
        num /= 10;
    }
    if (largestOdd == -1)
    {
        return "";
    }

    return to_string(largestOdd);
}

int main()
{
    string str;
    cin >> str;

    cout << largeOddNum(str) << endl;

    return 0;
}
