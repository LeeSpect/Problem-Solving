# ----------------------------------------------------------------------------------------------------
# 틀린 코드: make_dp를 두 번 돌게 했지만, RGB 색상은 3개이므로 3번 돌아야 한다.
# 3번 돌릴 때마다 처음 방문하는 색상만 0으로 두고 나머지는 inf로 둬야한다.

import sys; input=sys.stdin.readline

def make_dp(i,RGBs,dp,n):
    temp=[0,0,0]
    if i==n-2:
        for j in range(3):
            pos=[0,1,2]
            pos.remove(j)
            mini=1001
            for k in pos:
                if dp[k][1]==j:
                    continue
                mini=min(dp[k][0],mini)
            if mini==1001:
                temp[j]=mini
            else:
                temp[j]=mini+RGBs[j]
    else:
        for v in range(3):
            temp[v]=(RGBs[v]+min(dp[v-1],dp[v-2])[0],min(dp[v-1],dp[v-2])[1])
    dp=temp[:]
    return dp

def main():
    n=int(input())
    dp=list(map(int,input().split()))
    first_dp_temp=dp[:]
    for i in range(3):
        dp[i]=(dp[i],i)
    dp2=[0,0,0]
    for i in range(n-1):
        RGBs=list(map(int,input().split()))
        dp=make_dp(i,RGBs,dp,n)
        if i==0:
            for q in range(3):
                dp2[q]=(RGBs[q],q)
        else:
            dp2=make_dp(i-1,RGBs,dp2,n)
    dp2=make_dp(n-2,first_dp_temp,dp2,n)
    print(min(min(dp),min(dp2)))

if __name__=='__main__':
    main()
    
# ----------------------------------------------------------------------------------------------------
# 수정 코드: 3번 돌았다. make_dp에서, dp에는 i에 해당하는 인덱스 값에만 RGBs의 값을 대입한다.
# 그리고 아래로 쭉 내려가다 보면 처음에 i번째 집을 방문한 경우의 값들만 나온다.
# 마지막 집은 첫 번째 집과 겹치면 안 되므로 i값을 제외한 나머지 dp값들을 비교하여 최소값을 도출한다. 이것을 3번 반복한다.

import sys; input=sys.stdin.readline

def make_dp(n,RGBs,i,ans):
    dp=[[float('inf')]*3 for _ in range(n)]
    dp[0][i]=RGBs[0][i]
    for j in range(1,n):
        for q in range(3):
	        dp[j][q]=RGBs[j][q]+min(dp[j-1][q-1],dp[j-1][q-2])
    for k in range(3):
        if k!=i:
            ans=min(ans,dp[-1][k])
    return ans

def main():
    n=int(input())
    RGBs=[list(map(int,input().split())) for _ in range(n)]
    ans=float('inf')
    for i in range(3):
        ans=make_dp(n,RGBs,i,ans)
    print(ans)

if __name__=='__main__':
    main()
