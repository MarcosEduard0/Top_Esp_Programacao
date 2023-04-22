#include <iostream>
#include <vector>
#include <set>

using namespace std;

int main()
{
    int num_test_cases;
    cin >> num_test_cases;

    while (num_test_cases--)
    {
        int m, n;
        cin >> m >> n;

        vector<int> items(m);
        for (int i = 0; i < m; i++)
            cin >> items[i];

        multiset<int> sorted;
        auto it = items.begin();        // iterador para percorrer items
        auto sortedIt = sorted.begin(); // iterador para percorrer sorted

        for (int i = 0; i < n; i++)
        {
            int v;
            cin >> v;

            // Adiciona novos elementos ao multiset até que sua size seja v
            while (sorted.size() < v)
            {
                sorted.insert(*it);

                // Verifica se o elemento que acabou de ser inserido é menor que o elemento
                // para o qual sortedIt está apontando. Se for, decrementa sortedIt.
                if (sortedIt == sorted.end() || *sortedIt > *it)
                    sortedIt--;

                it++;
            }

            cout << *sortedIt << endl;
            sortedIt++;
        }

        if (num_test_cases > 0)
            cout << endl;
    }

    return 0;
}
