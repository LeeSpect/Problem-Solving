import sys; input=sys.stdin.readline

def sol(M,l,i,n,ans):
    for j in range(i,n):
        if M==1:
            print(ans+str(l[j]))
            continue
        else:
            sol(M-1,l,j,n,ans+str(l[j])+' ')

def main():
    N,M=map(int,input().split())
    l=list(set(list(map(int,input().split()))))
    l.sort()
    n=len(l)
    ans=''
    sol(M,l,0,n,ans)

if __name__=='__main__':
    main()
    
#----------------------------------------------------------------------------------------------------

import sys; input=sys.stdin.readline
from itertools import combinations_with_replacement

n,m=map(int,input().split())
l=list(map(int,input().split()))
l.sort()
ansl=list(set(combinations_with_replacement(l,m)))
ansl.sort()
t=len(ansl)
for i in range(t):
    print(*ansl[i])
