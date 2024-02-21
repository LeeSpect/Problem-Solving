import sys
input = sys.stdin.readline

while 1:
    n = int(input())
    if not n:
        break
    l = list(map(int, input().split()))
    x = int(input())
    temp = l[x - 1] + 1

    ans = 0
    for i in l:
        ans += temp - i if temp > i else 0

    print(ans)
