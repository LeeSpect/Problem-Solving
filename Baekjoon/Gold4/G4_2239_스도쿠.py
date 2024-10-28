# 각 행과 열을 모두 집합으로 만들어서 중복을 빠르게 검사할 수 있도록 한다.
# DFS로 백트래킹한다.
import sys; input=sys.stdin.readline

def DFS(G,sudo_r,sudo_c,sudo_3x3,r,c):
    if c==9:
        c=0
        r+=1
    if r==9:
        for i in range(9):
            for j in range(9):
                print(G[i][j],end='')
            print()
        exit()
    if not G[r][c]:
        for k in range(1,10):
            if k not in sudo_r[r] and k not in sudo_c[c] and k not in sudo_3x3[r//3][c//3]:
                sudo_r[r].add(k)
                sudo_c[c].add(k)
                sudo_3x3[r//3][c//3].add(k)
                G[r][c]=k
                DFS(G,sudo_r,sudo_c,sudo_3x3,r,c+1)
                sudo_r[r].discard(k)
                sudo_c[c].discard(k)
                sudo_3x3[r//3][c//3].discard(k)
                G[r][c]=0
    else:
        DFS(G,sudo_r,sudo_c,sudo_3x3,r,c+1)

def main():
    G=[list(input().rstrip()) for _ in range(9)]
    sudo_r=[set() for _ in range(9)]
    sudo_c=[set() for _ in range(9)]
    sudo_3x3=[[set() for i in range(3)] for j in range(3)]
    for i in range(9):
        for j in range(9):
            G[i][j]=int(G[i][j])
            if G[i][j]:
                sudo_r[i].add(G[i][j])
                sudo_c[j].add(G[i][j])
                sudo_3x3[i//3][j//3].add(G[i][j])
    DFS(G,sudo_r,sudo_c,sudo_3x3,0,0)

if __name__=='__main__':
    main()
