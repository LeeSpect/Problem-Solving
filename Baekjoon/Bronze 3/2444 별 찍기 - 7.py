n = int(input())
for i in range(n):
    print(' '*(n-i-1) + '*'*(1+2*i))
for i in range(1, n):
    print(' '*i + '*'*(1+2*(n-1-i)))
