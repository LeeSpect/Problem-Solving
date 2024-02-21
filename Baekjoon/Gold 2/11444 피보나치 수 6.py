# 참조: https://zzonglove.tistory.com/32 [행렬 멱법을 이용한 피보나치 값 구하기]
# 행렬곱을 이용하여 피보나치 값을 구할 수 있다.
import sys; input=sys.stdin.readline

def fib(n,memo):
    if n in memo:
        return memo[n]
    if n%2:
        k=(n+1)//2
        ans=(((fib(k,memo)%1000000007)**2)%1000000007 + (fib(k-1,memo)%1000000007)**2%1000000007)%1000000007
        memo[n]=ans
        return ans
    else:
        k=n//2
        f=fib(k,memo)%1000000007
        ans=(f*(f+(fib(k-1,memo)%1000000007*2)%1000000007)%1000000007)%1000000007
        memo[n]=ans
        return ans

def main():
    n = int(input())
    memo={1:1, 2:1, 3:2}
    print(fib(n,memo))
    
if __name__=='__main__':
    main()
