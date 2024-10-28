# ----------------------------------------------------------------------------------------------------
# 틀린 코드: 인덱스 에러
import sys; input=sys.stdin.readline

def LCS(string1,string2,leng1,leng2):
    dp=[[] for _ in range(leng2+1)]
    for i in range(leng1+1):
        for j in range(leng2+1):
            if i==0 or j==0:
                dp[i].append(0)
            elif string1[i-1]==string2[j-1]:
                dp[i].append(dp[i-1][j-1]+1)
            else:
                dp[i].append(max(dp[i][j-1], dp[i-1][j]))
    return dp

def main():
    string1=input().rstrip()
    string2=input().rstrip()
    leng1,leng2=len(string1),len(string2)
    dp=LCS(string1,string2,leng1,leng2)
    print(dp[-1][-1])
    r,c=leng1,leng2
    ans=''
    while dp[r][c]!=0:
        if dp[r][c]>dp[r-1][c] and dp[r][c]>dp[r][c-1]:
            ans=string1[r-1]+ans
            r-=1
            c-=1
        elif dp[r][c]==dp[r-1][c]:
            r-=1
        elif dp[r][c]==dp[r][c-1]:
            c-=1
    print(ans)

if __name__=='__main__':
    main()
    
# ----------------------------------------------------------------------------------------------------
# 수정 코드: LCS 함수에서 dp=[[] for in range(leng2+1)]를 dp=[[] for in range(leng1+1)]로 수정하였다.
import sys; input=sys.stdin.readline

def LCS(string1,string2,leng1,leng2):
    dp=[[] for _ in range(leng1+1)]
    for i in range(leng1+1):
        for j in range(leng2+1):
            if i==0 or j==0:
                dp[i].append(0)
            elif string1[i-1]==string2[j-1]:
                dp[i].append(dp[i-1][j-1]+1)
            else:
                dp[i].append(max(dp[i][j-1], dp[i-1][j]))
    return dp

def main():
    string1=input().rstrip()
    string2=input().rstrip()
    leng1,leng2=len(string1),len(string2)
    dp=LCS(string1,string2,leng1,leng2)
    print(dp[-1][-1])
    r,c=leng1,leng2
    ans=''
    while dp[r][c]!=0:
        if dp[r][c]>dp[r-1][c] and dp[r][c]>dp[r][c-1]:
            ans=string1[r-1]+ans
            r-=1
            c-=1
        elif dp[r][c]==dp[r-1][c]:
            r-=1
        elif dp[r][c]==dp[r][c-1]:
            c-=1
    print(ans)

if __name__=='__main__':
    main()
