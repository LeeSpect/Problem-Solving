t = int(input())
for _ in range(t):
    n = int(input())
    s = bin(n)[2:]
    s = s[::-1]
    for i in range(len(s)):
        if s[i] == '1':
            print(i, end=' ')
