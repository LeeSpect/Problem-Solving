# DFS로 백트래킹
# pypy로 통과

# ----------------------------------------------------------------------------------------------------
# 틀린 코드(시간 초과)
import sys; input=sys.stdin.readline

rpos,cpos=[1,-1,0,0],[0,0,1,-1]

def DFS(G,R,C,visited_pos,visited_alp,r,c,cnt,max_cnt,cosmos):
    cnt+=1
    visited_pos.add((r,c))
    visited_alp.add(G[r][c])
    for i in range(4):
        new_r,new_c=r+rpos[i],c+cpos[i]
        if 0<=new_r<R and 0<=new_c<C and (new_r,new_c) not in visited_pos and G[new_r][new_c] not in visited_alp:
            max_cnt=DFS(G,R,C,visited_pos,visited_alp,new_r,new_c,cnt,max_cnt,cosmos)
            if max_cnt==cosmos:
                print(max_cnt)
                exit()
    visited_pos.discard((r,c))
    visited_alp.discard(G[r][c])
    return max(max_cnt,cnt)

def main():
    R,C=map(int,input().split())
    G=[]
    for _ in range(R):
        G.append(list(input().rstrip()))
    cos=set()
    for i in range(R):
        for j in range(C):
            cos.add(G[i][j])
    cosmos=len(cos)
    visited_pos=set()
    visited_alp=set()
    r,c,cnt,max_cnt=0,0,0,0
    print(DFS(G,R,C,visited_pos,visited_alp,r,c,cnt,max_cnt,cosmos))

if __name__=='__main__':
    main()

# ----------------------------------------------------------------------------------------------------
# 수정 코드: visited_pos는 불필요하므로 삭제, visited_alp를 아스키코드로 접근하는 리스트로 
import sys; input=sys.stdin.readline

rpos,cpos=[1,-1,0,0],[0,0,1,-1]

def DFS(G,R,C,visited_alp,r,c,cnt,cosmos, max_cnt):
    cnt+=1
    for i in range(4):
        new_r,new_c=r+rpos[i],c+cpos[i]
        if 0<=new_r<R and 0<=new_c<C and visited_alp[ord(G[new_r][new_c])-65]==0:
            visited_alp[ord(G[new_r][new_c])-65]=1
            max_cnt=DFS(G,R,C,visited_alp,new_r,new_c,cnt,cosmos,max_cnt)
            visited_alp[ord(G[new_r][new_c])-65]=0
            if max_cnt==cosmos:
                print(max_cnt)
                exit()
    return max(max_cnt,cnt)

def main():
    R,C=map(int,input().split())
    G=[list(input().rstrip()) for _ in range(R)]
    cos=set()
    for i in G:
        for j in i:
            cos.add(j)
    cosmos=len(cos)
    visited_alp=[0]*26
    visited_alp[ord(G[0][0])-65]=1
    r,c,cnt,max_cnt=0,0,0,0
    print(DFS(G,R,C,visited_alp,r,c,cnt,cosmos,max_cnt))

if __name__=='__main__':
    main()
