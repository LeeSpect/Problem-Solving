import sys; input=sys.stdin.readline

def find_zero(sols,start,end):
    almost_zero=float('inf')
    s,e=start,end
    while start<end:
        a=sols[start]
        b=sols[end]
        if a+b==0:
            s,e=a,b
            break
        if almost_zero>abs(a+b):
            almost_zero=abs(a+b)
            s,e=a,b
        if a+b<0:
            start+=1
        else:
            end-=1
    print(s,e)

def main():
    N=int(input())
    sols=list(map(int,input().split()))
    start,end=0,N-1
    find_zero(sols,start,end)

if __name__=='__main__':
    main()
