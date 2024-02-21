import sys

x = int(sys.stdin.readline())
y = int(sys.stdin.readline())
z = int(sys.stdin.readline())

a = (x-y+z-1)//z

print(250 if x-y <=0 else 250+a*100)
