import sys
input=sys.stdin.readline

l=[i for i in range(1, 31)]
for i in range(28):
    n = int(input())
    l.remove(n)
print(l[0])
print(l[1])
