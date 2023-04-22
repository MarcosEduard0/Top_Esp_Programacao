
while True:
    s = input()
    if s == '.':
        break
    string_length = len(s)
    max_length = 1
    for i in range(1, string_length):
        while s[i % max_length] != s[i]:
            max_length += 1
    if string_length % max_length != 0:
        print("1")
    else:
        print(string_length // max_length)
