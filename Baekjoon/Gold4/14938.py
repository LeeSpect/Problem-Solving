import sys; input=sys.stdin.readline

def dfs(x,m,roads,items,visited,maxi):
    if x not in visited:
        visited.add(x)
        maxi+=items[x]
    for road in roads[x]:
        if m-road[1]>=0:
            maxi=dfs(road[0],m-road[1],roads,items,visited,maxi)
    return maxi

def main():
    n,m,r=map(int,input().split())
    items=[0]
    items.extend(list(map(int,input().split())))
    roads=[[] for i in range(n+1)]
    for i in range(r):
        a,b,l=map(int,input().split())
        roads[a].append((b,l))
        roads[b].append((a,l))
    ans=0
    for x in range(1,n+1):
        ans=max(ans,dfs(x,m,roads,items,set(),0))
    print(ans)
    
if __name__=='__main__':
    main()
