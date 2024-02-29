import sys

n = int(sys.stdin.readline())
if n == 0: print(0)
else: 
    ans = 1
    for i in range(1, n+1):
        ans *= i
    print(ans%10)
