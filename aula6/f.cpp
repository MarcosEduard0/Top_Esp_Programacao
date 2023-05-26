#include <iostream>
#include <vector>
using namespace std;

void sieve(vector<bool> &isPrime)
{
    int n = isPrime.size();
    isPrime[0] = isPrime[1] = false;

    for (int i = 2; i * i < n; ++i)
    {
        if (isPrime[i])
        {
            for (int j = i * i; j < n; j += i)
            {
                isPrime[j] = false;
            }
        }
    }
}

int main()
{
    const int mx = 10000001;
    vector<bool> isPrime(mx, true);
    sieve(isPrime);

    int n;
    while (cin >> n)
    {
        if (n < 8)
        {
            cout << "Impossible.\n";
        }
        else
        {
            int a, b, s, c = 0;
            if (n % 2 == 0)
            {
                a = 2;
                b = 2;
            }
            else
            {
                a = 2;
                b = 3;
            }
            s = n - (a + b);
            for (int i = 2; i < s; ++i)
            {
                if (isPrime[i] && isPrime[s - i])
                {
                    cout << a << " " << b << " " << i << " " << s - i << "\n";
                    c = 1;
                    break;
                }
            }
            if (!c)
                cout << "Impossible.\n";
        }
    }

    return 0;
}
