import sys
input=sys.stdin.readline

def correct_palindrome(nums,dp,S,E):
    if (S+E)%2:
        cor_S,cor_E=(S+E)//2,(S+E)//2+1
    else:
        cor_S,cor_E=(S+E)//2,(S+E)//2
    flag=-1
    while S<=cor_S:
        if flag==0:
            dp[cor_S][cor_E]=0
        else:
            if nums[cor_S]==nums[cor_E]:
                dp[cor_S][cor_E]=1
            else:
                dp[cor_S][cor_E]=0
                flag=0
        cor_S-=1
        cor_E+=1
    return dp

def main():
    N=int(input())
    nums=list(map(int,input().split()))
    dp=[[-1]*N for i in range(N)]
    for i in range(N):
        dp[i][i]=1
    M=int(input())
    for _ in range(M):
        S,E=map(int,input().split())
        if dp[S-1][E-1]==-1:
            dp=correct_palindrome(nums,dp,S-1,E-1)
        if dp[S-1][E-1]==0:
            print(0)
        else:
            print(1)

if __name__=='__main__':
    main()
