a,b,c = map(int, input().split())
if a-b >= b: b = a-b
if a-c >= c: c = a-c
print(4*b*c)
