# 1,417,752 KB / 732 ms
import sys
import math
input = sys.stdin.readline

def init(node:int, start:int, end:int):
    if start == end:
        trees[node] = numbers[start]
        return
    init(node*2, start, (start+end)//2)
    init(node*2+1, (start+end)//2+1, end)
    trees[node] = trees[node*2] * trees[node*2+1] % 1000000007

def query(node:int, start:int, end:int, left:int, right:int):
    if start > right or end < left: return 1
    elif left <= start and end <= right: return trees[node]
    lsum = query(node*2, start, (start+end)//2, left, right)
    rsum = query(node*2+1, (start+end)//2+1, end, left, right)
    return lsum * rsum % 1000000007

def update(node:int, start:int, end:int, idx:int, val:int):
    if idx < start or end < idx: return
    elif start == end:
        numbers[idx] = val
        trees[node] = val
        return
    update(node*2, start, (start+end)//2, idx, val)
    update(node*2+1, (start+end)//2+1, end, idx, val)
    trees[node] = trees[node*2] * trees[node*2+1] % 1000000007
    

N, M, K = map(int, input().split())
numbers = [int(input()) for _ in range(N)]
h = 1 <<( math.ceil(math.log2(N))+1 )
trees = [0] * h
init(1, 0, N-1)
M += K
for _ in range(M):
    a, b, c = map(int, input().split())
    # print(trees)
    if a == 1:
        update(1, 0, N-1, b-1, c)
    else:
        print(query(1, 0, N-1, b-1, c-1)%1000000007)