A,B = map(int, input().split())
m = A*B
L = list(map(int, input().split()))
for i in L:
    print(i-m, end=' ')
