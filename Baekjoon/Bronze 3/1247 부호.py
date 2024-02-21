import sys

for i in range(3):
    n = int(input())
    data = [int(sys.stdin.readline()) for j in range(n)]
    s = sum(data)
    if s == 0:
        print(0)
    elif s < 0:
        print('-')
    else: print('+')
