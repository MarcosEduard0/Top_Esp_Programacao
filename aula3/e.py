import sys

for line in sys.stdin:
    n, string = line.strip().split()
    n = int(n)
    record = {}
    for i in range(len(string)-n+1):
        substr = string[i:i+n]
        if substr in record:
            record[substr] += 1
        else:
            record[substr] = 1
    max_count = 0
    for substr, count in record.items():
        if count > max_count:
            max_count = count
            max_substr = substr
    print(max_substr)