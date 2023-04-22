#include <iostream>
#include <string>
#include <map>

using namespace std;

string mensagem, senha, str_aux;
map<string, int> record;

int main()
{
    int n;

    while (cin >> n)
    {
        int maxn = -1;
        record.clear();
        cin >> mensagem;
        for (int i = 0; i < mensagem.length() - n; i++)
        {
            str_aux = mensagem.substr(i, n);
            record[str_aux]++;
        }
        map<string, int>::iterator it;
        for (it = record.begin(); it != record.end(); it++)
            if (it->second > maxn)
            {
                maxn = it->second;
                senha = it->first;
            }
        cout << senha << endl;
    }
    return 0;
}