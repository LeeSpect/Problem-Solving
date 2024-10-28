import sys

t = int(sys.stdin.readline())
for i in range(t):
    a,b = map(int,sys.stdin.readline().split())
    if (a<=2 and b<=1) or (a<=1 and b<=2):
        print('Yes')
    else:
        print('No')
