# 트리의 지름을 구하는 알고리즘이 따로 있다.
# 임의의 점 x에서 가장 먼 y를 찾고, y에서 가장 먼 z를 찾은 후, y에서 z까지의 거리를 구하면 된다. 따라서 DFS를 두 번 돌아서 정답을 구할 수 있다.

import sys; input=sys.stdin.readline

def DFS(T,start,maxi,far,cost,visited):
    visited.add(start)
    for i in T[start]:
        if i[0] not in visited:
            maxi,far,visited=DFS(T,i[0],maxi,far,cost+i[1],visited)
            if maxi<cost+i[1]:
                maxi=cost+i[1]
                far=i[0]
    return maxi,far,visited

def main():
    V=int(input())
    T=[[] for _ in range(V+1)]
    for _ in range(V):
        l=list(map(int,input().split()))
        idx=1
        while l[idx]!=-1:
            T[l[0]].append((l[idx],l[idx+1]))
            idx+=2
    maxi,far,visited=DFS(T,1,0,0,0,set())
    print(DFS(T,far,0,0,0,set())[0])

if __name__=='__main__':
    main()
