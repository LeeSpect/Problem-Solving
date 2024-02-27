import sys; input=sys.stdin.readline

def main():
    t=int(input())
    l=list(map(int,input().split()))
    dp=[i for i in range(51)]
    for i in l:
        dp[i]-=1
    for q in range(50,-1,-1):
        if dp[q]==0:
            print(q)
            exit()
    print(-1)

if __name__=='__main__':
    main()
