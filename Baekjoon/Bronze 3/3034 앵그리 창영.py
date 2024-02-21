n,w,h = map(int, input().split())
limit = (w**2 + h**2)**0.5
for i in range(n):
    a = int(input())
    if limit < a: print('NE')
    else: print('DA')
