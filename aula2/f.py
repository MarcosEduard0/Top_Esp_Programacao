import string as s
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
            thisval = thisval*10 + (ord(ch) - ord('0'))

    thisval *= sign
    val += thisval
    child1 = read_tree(val)

    while True:
        ch = sys.stdin.read(1)
        if ch == '(':
            child2 = read_tree(val)
            break
    print('valor:', val)
    if not child1 and not child2 and val == SUM:
        yes = True

    while True:
        ch = sys.stdin.read(1)
        if ch == ')':
            return True


while True:
    try:
        while True:
            ch = sys.stdin.read(1)
            if ch == ' ' or ch == '\n':
                break
            if ch.isdigit():
                SUM = SUM*10 + (ord(ch) - ord('0'))
        # SUM = int(input())
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
