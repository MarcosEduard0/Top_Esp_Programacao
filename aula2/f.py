import sys

yes = False

def read_tree(val, sum):
    global ch, yes
    child1, child2 = False, False
    thisval, sign = 0, 1
    while True:
        ch = sys.stdin.read(1)
        if ch == ' ' or ch == '\n':
            continue
        if ch == ')':
            return False  # null
        if ch == '(':
            break
        if ch == '-':
            sign = -1
        if ch.isdigit():
            thisval = thisval*10 + int(ch)

    thisval *= sign
    val += thisval

    child1 = read_tree(val, sum)
    while True:
        ch = sys.stdin.read(1)
        if ch == '(':
            break
    
    child2 = read_tree(val, sum)
    
    if not child1 and not child2 and val == sum:
        yes = True

    while True:
        ch = sys.stdin.read(1)
        if ch == ')':
            return True


while True:
    try:
        SUM = 0
        while True:
            ch = sys.stdin.read(1)
            if ch == '\n':
                continue
            if ch == ' ':
                break
            if ch.isdigit():
                SUM = SUM*10 + int(ch)
            if ch == '':
                break # sair do loop se a linha estiver vazia

        if ch == '':
            break # sair do loop se a linha estiver vazia
               
        yes = False
        while True:
            ch = sys.stdin.read(1)
            if ch == '(':
                read_tree(0, SUM)
                break
        print("yes" if yes else "no")

    except:
        break
