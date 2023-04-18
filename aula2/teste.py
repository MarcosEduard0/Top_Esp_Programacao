import string as s
import sys

digitos = s.digits
soma = ''
thisval = 0
while True:
    ch = sys.stdin.read(1)
    if ch in digitos:
        soma += ch
    if ch == '(':
        break
    if ch == ' ' or ch == '\n':

        continue
    if ch == ')':
        break
    if ch == '-':
        sign = -1
    if ch.isdigit():
        thisval = thisval*10 + (ord(ch) - ord('0'))
soma = int(soma)
print(soma, thisval)
