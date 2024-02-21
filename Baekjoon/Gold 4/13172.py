import sys; input=sys.stdin.readline
from math import gcd

def sol(a,b):
    r1,r2,s1,s2,t1,t2,q1=1000000007,b,1,0,0,1,1000000007//b

    while r2>1:
        r1,r2=r2,r1%r2
        s1,s2=s2,s1-s2*q1
        t1,t2=t2,t1-t2*q1
        q1=r1//r2
        print('r1, r2:',r1,r2)
        print('s1, s2:',s1,s2)
        print('t1, t2:',t1,t2)
        print('q1:', q1)
    if t2<0: t2=1000000007+t2
    return ((t2%1000000007)*(a%1000000007))%1000000007

def main():
    t=int(input())
    ans=0
    for _ in range(t):
        N,S=map(int,input().split())
        g=gcd(N,S); N,S=N//g,S//g
        ans=(ans+sol(S,N))%1000000007
    print(ans)

if __name__=='__main__':
    main()
