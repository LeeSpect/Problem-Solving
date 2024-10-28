# 209,140 KB / 1,580 ms
import sys
input = sys.stdin.readline

def init(node, start, end):
    if start == end:
        tree[node] = [L[start][0], L[start][1]]
        return
    init(node*2, start, (start+end)//2)
    init(node*2+1, (start+end)//2+1, end)
    
    if tree[node*2][0] < tree[node*2+1][0]: # 왼쪽 자식 노드가 더 작으면
        tree[node] = [tree[node*2][0], tree[node*2][1]] # 왼쪽 자식 노드의 값과 인덱스 저장
    elif tree[node*2][0] > tree[node*2+1][0]:
        tree[node] = [tree[node*2+1][0], tree[node*2+1][1]] # 오른쪽 자식 노드의 값과 인덱스 저장
    else:
        if tree[node*2][1] < tree[node*2+1][1]: # 값이 같으면 인덱스가 작은 것을 저장
            tree[node] = [tree[node*2][0], tree[node*2][1]]
        else:
            tree[node] = [tree[node*2+1][0], tree[node*2+1][1]]

def update(node, start, end, idx, val):
    if idx < start or idx > end: return
    if start == end:
        tree[node] = [val, idx]
        return
    update(node*2, start, (start+end)//2, idx, val)
    update(node*2+1, (start+end)//2+1, end, idx, val)
    
    if tree[node*2][0] < tree[node*2+1][0]: # 왼쪽 자식 노드가 더 작으면
        tree[node] = [tree[node*2][0], tree[node*2][1]] # 왼쪽 자식 노드의 값과 인덱스 저장
    elif tree[node*2][0] > tree[node*2+1][0]:
        tree[node] = [tree[node*2+1][0], tree[node*2+1][1]]
    else:
        if tree[node*2][1] < tree[node*2+1][1]:
            tree[node] = [tree[node*2][0], tree[node*2][1]]
        else:
            tree[node] = [tree[node*2+1][0], tree[node*2+1][1]]

def query(node, start, end, left, right):
    if left > end or right < start: return [float('inf'), -1]
    if left <= start and end <= right: return tree[node]
    
    l = query(node*2, start, (start+end)//2, left, right)
    r = query(node*2+1, (start+end)//2+1, end, left, right)
    
    if l[0] < r[0]: return l
    elif l[0] > r[0]: return r
    else:
        if l[1] < r[1]: return l
        else: return r


N = int(input())
A = list(map(int, input().split()))
M = int(input())

tree = [0] * 4*N # 세그먼트 트리
L = [[A[i], i] for i in range(len(A))] # 값과 인덱스를 저장한 리스트

init(1, 0, N-1) # 세그먼트 트리 초기화

for _ in range(M):
    a, b, c = map(int, input().split())
    if a==1:
        update(1, 0, N-1, b-1, c)
    else:
        ans = query(1, 0, N-1, b-1, c-1)
        print(ans[1]+1)