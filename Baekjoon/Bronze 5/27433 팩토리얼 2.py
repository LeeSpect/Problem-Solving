# 틀린 코드

import sys; input = sys.stdin.readline

def fac(k):
    if k == 1:
        return k
    return k * fac(k-1)

n = int(input())
print(fac(n))

# ----------------------------------------------------------------------------------------------------
# 수정 코드

import sys; input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def fac(k):
    if k == 0:
        return 1
    if k == 1:
        return k
    return k * fac(k-1)

n = int(input())
print(fac(n))
