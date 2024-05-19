import sys
from string import ascii_uppercase

input = sys.stdin.readline

T = int(input())
alpha = list(ascii_uppercase)

def solve(x, a, b):
    return (a * x + b) % 26

for _ in range(T):
    ans = []
    a, b = map(int, input().split())
    s = input().rstrip()
    for i in s:
        ans.append(alpha[solve(alpha.index(i),a,b)])
    print(''.join(ans))