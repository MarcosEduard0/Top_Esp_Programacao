#include <cstdio>
#include <vector>
using namespace std;
const int M = 100005;
const int N = 10000005;
#define pb push_back
int read()
{
    int x = 0, f = 1;
    char c;
    while ((c = getchar()) < '0' || c > '9')
    {
        if (c == '-')
            f = -1;
    }
    while (c >= '0' && c <= '9')
    {
        x = (x << 3) + (x << 1) + (c ^ 48);
        c = getchar();
    }
    return x * f;
}
int n, m, cnt, tot, f[M];
vector<int> g[N], vc[M << 2];
int Ind, num[M], siz[M], son[M], top[M], fa[M], dep[M];
int k, scc, dfn[N], low[N], col[N], s[N], in[N];
struct edge
{
    int v, next;
} e[M << 1];
void add(int u, int v)
{
    g[u].pb(v);
    g[v ^ 1].pb(u ^ 1);
}
void dfs1(int u, int p)
{
    siz[u] = 1;
    fa[u] = p;
    dep[u] = dep[p] + 1;
    for (int i = f[u]; i; i = e[i].next)
    {
        int v = e[i].v;
        if (v == p)
            continue;
        dfs1(v, u);
        siz[u] += siz[v];
        if (siz[v] > siz[son[u]])
            son[u] = v;
    }
}
void dfs2(int u, int tp)
{
    top[u] = tp;
    num[u] = ++Ind;
    if (son[u])
        dfs2(son[u], tp);
    for (int i = f[u]; i; i = e[i].next)
        if (e[i].v ^ fa[u] && e[i].v ^ son[u])
            dfs2(e[i].v, e[i].v);
}
void ins(int i, int l, int r, int L, int R, int w)
{
    if (L > r || l > R)
        return;
    if (L <= l && r <= R)
    {
        vc[i].push_back(w);
        return;
    }
    int mid = (l + r) >> 1;
    ins(i << 1, l, mid, L, R, w);
    ins(i << 1 | 1, mid + 1, r, L, R, w);
}
void add(int u, int v, int w)
{
    while (top[u] ^ top[v])
    {
        if (dep[top[u]] < dep[top[v]])
            swap(u, v);
        ins(1, 1, n, num[top[u]], num[u], w);
        u = fa[top[u]];
    }
    if (dep[u] < dep[v])
        swap(u, v);
    if (u != v)
        ins(1, 1, n, num[v] + 1, num[u], w);
}
void build(int i, int l, int r, int p)
{
    int o = vc[i].size(), u = ++cnt, v = (cnt += o);
    if (o)
        add(v - 1 << 1, v << 1);
    else if (p)
        add(p << 1, v << 1);
    for (int j = 0; j < o; j++)
    {
        int w = vc[i][j];
        add(w, u + j << 1);
        if (j)
            add(u + j - 1 << 1, w ^ 1), add(u + j - 1 << 1, u + j << 1);
        else if (p)
            add(p << 1, u << 1), add(p << 1, w ^ 1);
    }
    if (l == r)
        return;
    int mid = (l + r) >> 1;
    build(i << 1, l, mid, v);
    build(i << 1 | 1, mid + 1, r, v);
}
void tarjan(int u)
{
    low[u] = dfn[u] = ++Ind;
    s[++k] = u;
    in[u] = 1;
    for (int v : g[u])
    {
        if (!dfn[v])
        {
            tarjan(v);
            low[u] = min(low[u], low[v]);
        }
        else if (in[v])
            low[u] = min(low[u], dfn[v]);
    }
    if (low[u] == dfn[u])
    {
        int v;
        scc++;
        do
        {
            v = s[k--];
            col[v] = scc;
            in[v] = 0;
        } while (u != v);
    }
}
signed main()
{
    n = cnt = read();
    for (int i = 1; i < n; i++)
    {
        int u = read(), v = read();
        e[++tot] = edge{v, f[u]}, f[u] = tot;
        e[++tot] = edge{u, f[v]}, f[v] = tot;
    }
    dfs1(1, 0);
    dfs2(1, 1);
    m = read();
    for (int i = 1; i <= m; i++)
    {
        add(read(), read(), i << 1);
        add(read(), read(), i << 1 | 1);
    }
    build(1, 1, n, 0);
    Ind = 0;
    for (int i = 1; i <= 2 * cnt; i++)
        if (!dfn[i])
            tarjan(i);
    for (int i = 1; i <= m; i++)
        if (col[i << 1] == col[i << 1 | 1])
        {
            puts("NO");
            return 0;
        }
    puts("YES");
    for (int i = 1; i <= m; i++)
        puts(col[i << 1] < col[i << 1 | 1] ? "1" : "2");
}