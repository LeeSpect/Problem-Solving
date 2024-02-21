import sys

t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    if n%2==0: print(f'{n} is even')
    else: print(f'{n} is odd')
