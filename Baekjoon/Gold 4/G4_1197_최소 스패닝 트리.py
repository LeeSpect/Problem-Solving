# https://techblog-history-younghunjo1.tistory.com/257 [서로소 집합 알고리즘을 활용한 사이클 판별]
# https://techblog-history-younghunjo1.tistory.com/262 [최소 신장 트리를 찾는 크루스칼(Kruskal) 알고리즘]
# 각 노드의 부모 노드를 저장하는 배열 준비(초기값으로 각 노드는 자신을 부모 노드로 갖는다), 모든 간선을 오름차순으로 정리
# 오름차순으로 정렬된 간선들을 순서대로 방문하면서 간선으로 연결된 두 노드의 부모 노드가 다르다면 트리에 포함, 부모 노드가 다르다면 Union한 후 트리에 포함시킨다.

# Union-Find를 처음 접했습니다.
# 우선 각 노드의 부모 노드를 저장하는 리스트 parents를 준비하고(초기값은 자기 자신) 모든 간선을 오름차순으로 정리합니다.
# 오름차순으로 정렬된 간선들을 순서대로 방문하면서 Union합니다. Union에서 간선으로 연결된 두 노드의 부모 노드가 같은 것을 확인하면, 간선을 트리에 포함할 시 순환이 발생하므로, False를 return 합니다.
# 두 노드의 부모 노드가 서로 다르다면, 두 노드 중 루트 노드에 더 적합한 노드를 찾아 parents를 수정하고 True를 return합니다. 
# 위와 같이 Union의 return 값이 True라면, 해당 간선은 최소 스패닝 트리를 구성하는 간선이라는 뜻입니다. weigh에 그 값을 더해줍니다.


import sys; input=sys.stdin.readline
import heapq

def find_parent(parents,node1):
    if parents[node1]!=node1:
        parents[node1]=find_parent(parents,parents[node1])
    return parents[node1]

def Union(parents,node1,node2):
    a=find_parent(parents,node1)
    b=find_parent(parents,node2)
    if a==b:
        return False
    elif a<b:
        parents[b]=a
    else:
        parents[a]=b
    return True

def main():
    V,E=map(int,input().split())
    parents=[i for i in range(V+1)]
    edges=[]
    for i in range(E):
        A,B,C=map(int,input().split())
        heapq.heappush(edges,(C,A,B))
    weigh=0
    while edges:
        cost,node1,node2=heapq.heappop(edges)
        if Union(parents,node1,node2):
            weigh+=cost
    print(weigh)

if __name__=='__main__':
    main()
