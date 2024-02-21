import sys; input=sys.stdin.readline

def bel(N,G):   # 벨만포드 
    dist=[999999999999999999999999999999999999999999999999999999999999999999999]*(N+1)
    for k in range(N):
        for i in range(1,N+1):
            for edge in G[i]:
                if dist[i]+edge[1]<dist[edge[0]]:
                    dist[edge[0]]=dist[i]+edge[1]
                    if k==N-1:
                        return 'YES'
    return 'NO'

def main():
    TC=int(input())
    for _ in range(TC):
        N,M,W=map(int,input().split())
        G=[[] for i in range(N+1)]
        for i in range(M):
            S,E,T=map(int,input().split())
            G[S].append((E,T))
            G[E].append((S,T))
        for j in range(W):
            S,E,T=map(int,input().split())
            G[S].append((E,-T))
        ans=bel(N,G)
        if ans=='YES':
            print('YES')
        else:
            print('NO')

if __name__=='__main__':
    main()
