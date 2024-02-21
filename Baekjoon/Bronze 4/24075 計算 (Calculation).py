import sys

a,b = map(int, sys.stdin.readline().split())

l = [a+b, a-b]
l.sort()
print(l[1])
print(l[0])
