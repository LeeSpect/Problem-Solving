import sys

def getting(n):
    soo = [False, False] + [True]*n
    for i in range(2, int(n**0.5)+1):
        if soo[i]:
            for j in range(i+i, n, i):
                soo[j] = False
    return [i for i in range(2, n) if soo[i]]
                
k,l = list(map(int, sys.stdin.readline().split()))

con = 0
alpa = 0
gl = getting(l)
for a in gl:
    if k%a == 0:
        con = 1
        alpa = a
        break
print('GOOD' if con == 0 else f'BAD {alpa}')
