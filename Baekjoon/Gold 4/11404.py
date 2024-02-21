import sys; input=sys.stdin.readline

def sol(G,n):
    for k in range(n):
        for i in range(n):
            if k==i:
                continue
            for j in range(n):
                if i==j or k==j:
                    continue
                G[i][j]=min(G[i][j],G[i][k]+G[k][j])
    return G

def main():
    n=int(input())
    m=int(input())
    G=[[] for j in range(n)]
    for i in range(n):
        for j in range(n):
            if i!=j:
                G[i].append(float('inf'))
            else:
                G[i].append(0)

    for _ in range(m):
        a,b,c=map(int,input().split())
        G[a-1][b-1]=min(G[a-1][b-1],c)

    l=sol(G,n)

    for i in range(n):
        for j in range(n):
            if G[i][j]==float('inf'):
                print(0,end=' ')
            else:
                print(G[i][j],end=' ')
        print()

if __name__=='__main__':
    main()
