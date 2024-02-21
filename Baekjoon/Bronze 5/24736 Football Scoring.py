import sys
input=sys.stdin.readline

for i in range(2):
    l=list(map(int,input().split()))
    print(l[0]*6+l[1]*3+l[2]*2+l[3]+l[4]*2, end=' ')
