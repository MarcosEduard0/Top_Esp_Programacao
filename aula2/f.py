import sys

SUM = 0
yes = False
ch = ''


def read_tree(val):
    global ch, yes, SUM
    child1 = False
    child2 = False
    thisval = 0
    sign = 1
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
    child1 = read_tree(val)

    while True:
        ch = sys.stdin.read(1)
        if ch == '(':
            child2 = read_tree(val)
            break
    if not child1 and not child2 and val == SUM:
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
            if ch == '':  # tentativa de finalização do programa
                exit()
            if ch == ' ':
                break
            if ch.isdigit():
                SUM = SUM*10 + int(ch)
        yes = False
        while True:
            ch = sys.stdin.read(1)
            if ch == '(':
                read_tree(0)
                break
        if yes:
            print("yes")
        else:
            print("no")

    except:
        break
