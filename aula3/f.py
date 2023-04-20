
while True:
    s = input()
    if s == '.':
        break
    s_length = len(s)
    max_length = 1
    for i in range(1, s_length):
        while s[i] != s[i % max_length]:
            max_length += 1
    if s_length % max_length != 0:
        print("1")
    else:
        print(s_length // max_length)
