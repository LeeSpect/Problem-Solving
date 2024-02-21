import sys; input=sys.stdin.readline

rpos,cpos=(1,-1,0,0),(0,0,1,-1)

def spread_dust(R,C,G):
    temp=[[0 for i in range(C)] for i in range(R)]
    for i in range(R):
        for j in range(C):
            if G[i][j]>0:
                cnt=0
                for q in range(4):
                    if 0<=i+rpos[q]<R and 0<=j+cpos[q]<C and G[i+rpos[q]][j+cpos[q]]!=-1:
                        cnt+=1
                        temp[i+rpos[q]][j+cpos[q]]+=G[i][j]//5
                G[i][j]-=G[i][j]//5*cnt
    for i in range(R):
        for j in range(C):
            G[i][j]+=temp[i][j]
    return G

def cleaning(R,C,G,cleaner):
    r,c=cleaner[0]-1,0
    con='up'
    while 1:
        if r==cleaner[0] and c==1:
            G[r][c]=0
            break
        if r==c==0:
            con='right'
        elif r==0 and c==C-1:
            con='down'
        elif r==cleaner[0] and c==C-1:
            con='left'   
        if con=='up':
            G[r][c]=G[r-1][c]
            r-=1
        elif con=='right':
            G[r][c]=G[r][c+1]
            c+=1
        elif con=='down':
            G[r][c]=G[r+1][c]
            r+=1
        else:
            G[r][c]=G[r][c-1]
            c-=1
    r,c=cleaner[1]+1,0
    con='down'
    while 1:
        if r==cleaner[1] and c==1:
            G[r][c]=0
            break
        if r==R-1 and c==0:
            con='right'
        elif r==R-1 and c==C-1:
            con='up'
        elif r==cleaner[1] and c==C-1:
            con='left'
        if con=='down':
            G[r][c]=G[r+1][c]
            r+=1
        elif con=='right':
            G[r][c]=G[r][c+1]
            c+=1
        elif con=='up':
            G[r][c]=G[r-1][c]
            r-=1
        else:
            G[r][c]=G[r][c-1]
            c-=1
    return G

def main():
    R,C,T=map(int,input().split())
    G=[list(map(int,input().split())) for i in range(R)]
    for i in range(2,R-2):
        if G[i][0]==-1:
            cleaner=(i,i+1)
            break
    for i in range(T):
        G=spread_dust(R,C,G)
        G=cleaning(R,C,G,cleaner)
    dust=0
    for i in range(R):
        for j in range(C):
            if G[i][j]!=-1:
                dust+=G[i][j]
    print(dust)

if __name__=='__main__':
    main()
