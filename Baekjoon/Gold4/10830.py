import sys; input=sys.stdin.readline

def power(G,B,N):
    if B==1:
        l=[[i%1000 for i in G[j]] for j in range(N)]
        return l
    
    g=[[0 for i in range(N)] for j in range(N)]
    l=power(G,B//2,N)
    for i in range(N):
        for j in range(N):
            for k in range(N):
                g[i][j]+=l[i][k]*l[k][j]
    if B%2==1:
        g2=[[0 for i in range(N)] for j in range(N)]
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    g2[i][j]+=g[i][k]*G[k][j]
        return [[i%1000 for i in g2[j]] for j in range(N)]
    else:
        return [[i%1000 for i in g[j]] for j in range(N)]

def main():
    N,B=map(int,input().split())
    G=[]
    for i in range(N):
        G.append(list(map(int,input().split())))
    G=power(G,B,N)
    for i in range(N):
        print(*G[i])

if __name__=='__main__':
    main()
