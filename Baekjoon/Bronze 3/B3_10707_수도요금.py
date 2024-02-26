a = int(input())
b = int(input())
c = int(input())
d = int(input())
p = int(input())

if p <= c:
    if a*p <= b:
        print(a*p)
    else:
        print(b)
else:
    if a*p <= b+d*(p-c):
        print(a*p)
    else:
        print(b+d*(p-c))
