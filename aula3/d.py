while True:
    try:
        row1 = input()
        row2 = input()
    except EOFError:
        break

    # Inicializa um dicionário para contar as ocorrências de cada letra
    count = {chr(i): 0 for i in range(ord('a'), ord('z')+1)}

    # Conta as ocorrências de cada letra na primeira linha
    for letter in row1:
        count[letter] += 1

    # Conta as ocorrências de cada letra na segunda linha, se ela estiver presente na primeira
    output = []
    for letter in row2:
        if count[letter] > 0:
            count[letter] -= 1
            output.append(letter)

    # Imprime as letras que aparecem nas duas linhas, em ordem alfabética
    output.sort()
    print(''.join(output))
