import sys; input=sys.stdin.readline
from itertools import combinations

rpos,cpos=[1,-1,0,0],[0,0,1,-1]

def sol(house_inf, chicken_inf, combination):
    mini=float('inf')
    for com in combination:
        wei=0
        for house in house_inf:
            step_wei=float('inf')
            for chicken in com:
                step_wei=min(step_wei,abs(house[0]-chicken[0])+abs(house[1]-chicken[1]))
            wei+=step_wei
        mini=min(wei,mini)
    print(mini)

def main():
    N,M=map(int,input().split())
    G=[]
    house_inf=[]
    chicken_inf=[]
    for i in range(N):
        G.append(list(map(int,input().split())))
        for j in range(N):
            if G[i][j]==1:
                house_inf.append((i,j))
            elif G[i][j]==2:
                chicken_inf.append((i,j))
    combination=list(combinations(chicken_inf,M))
    sol(house_inf,chicken_inf,combination)

if __name__=='__main__':
    main()
