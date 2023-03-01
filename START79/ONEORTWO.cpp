#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
int32_t main()
{
    int T = 1;
    cin >> T;
    while (T--)
    {
        ll x, y;
        cin >> x >> y;
        if (x == y)
        {
            if (x % 2 == 0)
            {

                cout << "CHEFINA" << endl;
            }
            else
            {
                cout << "CHEF" << endl;
            }
        }
        else if (x > y)
        {
            if (x - y >= 2)
            {
                cout << "CHEF" << endl;
            }
            else
            {
                if (x % 2)
                {
                    cout << "CHEFINA" << endl;
                }
                else
                {
                    cout << "CHEF" << endl;
                }
            }
        }
        else
        {
            if (y - x >= 2)
            {
                cout << "CHEFINA" << endl;
            }
            else
            {
                if (y % 2 == 0)
                {
                    cout << "CHEF" << endl;
                }
                else
                {
                    cout << "CHEFINA" << endl;
                }
            }
        }
    }
    return 0;
}