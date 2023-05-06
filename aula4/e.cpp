#include <iostream>
#include <cstring>
using namespace std;

const int maxn = 1024000;
int t, Case, Q, m, n, q, a, b, st[maxn << 2], lazy[maxn << 2];
string str, pirates;
char c;

void push(int x, int l, int r)
{
    if (lazy[x] == -1)
        return;
    int mid = (l + r) >> 1;
    if (lazy[x] == 2)
    {
        st[x << 1] = ((mid - l) + 1) - st[x << 1];
        st[x << 1 | 1] = (r - mid) - st[x << 1 | 1];
        if (lazy[x << 1] == 2)
            lazy[x << 1] = -1;
        else if (lazy[x << 1] != -1)
            lazy[x << 1] ^= 1;
        else
            lazy[x << 1] = 2;
        if (lazy[x << 1 | 1] == 2)
            lazy[x << 1 | 1] = -1;
        else if (lazy[x << 1 | 1] != -1)
            lazy[x << 1 | 1] ^= 1;
        else
            lazy[x << 1 | 1] = 2;
    }
    else
    {
        lazy[x << 1] = lazy[x];
        lazy[x << 1 | 1] = lazy[x];
        st[x << 1] = ((mid - l) + 1) * lazy[x << 1];
        st[x << 1 | 1] = (r - mid) * lazy[x << 1 | 1];
    }
    lazy[x] = -1;
    return;
}

void build(int x, int l, int r)
{
    lazy[x] = -1;
    if (l == r)
    {
        st[x] = pirates[l - 1] - '0';
        return;
    }
    int mid = (l + r) >> 1;
    build(x << 1, l, mid);
    build(x << 1 | 1, mid + 1, r);
    st[x] = st[x << 1] + st[x << 1 | 1];
}

void update1(int x, int l, int r, int ul, int ur, int d)
{
    if (ul <= l && r <= ur)
    {
        st[x] = (r - l + 1) * d;
        lazy[x] = d;
        return;
    }
    push(x, l, r);
    int mid = (l + r) >> 1;
    if (ul <= mid)
        update1(x << 1, l, mid, ul, ur, d);
    if (mid < ur)
        update1(x << 1 | 1, mid + 1, r, ul, ur, d);
    st[x] = st[x << 1] + st[x << 1 | 1];
}

void update2(int x, int l, int r, int ul, int ur)
{
    if (ul <= l && r <= ur)
    {
        st[x] = (r - l + 1) - st[x];
        if (lazy[x] == 2)
            lazy[x] = -1;
        else if (lazy[x] != -1)
            lazy[x] ^= 1;
        else
            lazy[x] = 2;
        return;
    }
    push(x, l, r);
    int mid = (l + r) >> 1;
    if (ul <= mid)
        update2(x << 1, l, mid, ul, ur);
    if (mid < ur)
        update2(x << 1 | 1, mid + 1, r, ul, ur);
    st[x] = st[x << 1] + st[x << 1 | 1];
}

int query(int x, int l, int r, int ql, int qr)
{
    if (ql <= l && r <= qr)
    {
        return st[x];
    }
    push(x, l, r);
    int mid = (l + r) >> 1;
    int ret = 0;
    if (ql <= mid)
        ret += query(x << 1, l, mid, ql, qr);
    if (mid < qr)
        ret += query(x << 1 | 1, mid + 1, r, ql, qr);
    return ret;
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cin >> t;
    while (t--)
    {
        Case++;
        cout << "Case " << Case << ":\n";
        cin >> m;
        pirates = "";
        for (int i = 0; i < m; i++)
        {
            cin >> n;
            cin >> str;
            for (int i = 0; i < n; i++)
            {
                pirates += str;
            }
        }
        n = pirates.length();
        build(1, 1, n);
        cin >> q;
        Q = 0;
        for (int i = 0; i < q; i++)
        {
            cin >> c >> a >> b;
            a++;
            b++;
            if (c == 'F')
                update1(1, 1, n, a, b, 1);
            else if (c == 'E')
                update1(1, 1, n, a, b, 0);
            else if (c == 'I')
                update2(1, 1, n, a, b);
            else if (c == 'S')
            {
                Q++;
                cout << "Q" << Q << ": " << query(1, 1, n, a, b) << "\n";
            }
        }
    }
}