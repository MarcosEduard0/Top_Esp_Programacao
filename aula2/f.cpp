#include <iostream>
using namespace std;

#define i64 long long

int SOMA, flag;
char ch;

bool recursive_tree(const i64 valor)
{
    bool NoEsquerdo = false, NoDireito = false;
    int val_atual = 0, sign = 1;
    while ((ch = getchar()) != EOF)
    {
        if (ch == ' ' || ch == '\n')
            continue;
        if (ch == ')')
            return false;
        if (ch == '(')
            break;
        if (ch == '-')
            sign = -1;
        if (isdigit(ch))
            val_atual = val_atual * 10 + (ch - '0');
    }
    const i64 novo_valor = valor + static_cast<i64>(val_atual * sign);
    NoEsquerdo = recursive_tree(novo_valor);
    while ((ch = getchar()) != EOF && ch != '(')
        ;
    NoDireito = recursive_tree(novo_valor);

    if (!NoEsquerdo && !NoDireito && novo_valor == SOMA)
        flag = 1;
    while ((ch = getchar()) != EOF && ch != ')')
        ;
    return true;
}

int main()
{
    while (scanf("%d ", &SOMA) != EOF)
    {
        flag = 0;
        while ((ch = getchar()) != EOF && ch != '(')
            ;
        recursive_tree(0);
        if (flag)
            puts("yes");
        else
            puts("no");
    }
    return 0;
}
