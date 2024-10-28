import sys
input=sys.stdin.readline

a=int(input())
b=int(input())
s=a*8+b*3
if s>28:
    print(s-28)
else:
    print(0)
