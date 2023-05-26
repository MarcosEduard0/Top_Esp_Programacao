import math

while True:
    n = int(input())
    if n == 0:
        break

    root = int(math.sqrt(n))
    if root * root == n:
        print("yes")
    else:
        print("no")
