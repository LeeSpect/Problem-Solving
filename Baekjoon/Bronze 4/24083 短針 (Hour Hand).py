import sys

x = int(sys.stdin.readline())
y = int(sys.stdin.readline())

print(12 if (x+y)%12 == 0 else (x+y)%12)
