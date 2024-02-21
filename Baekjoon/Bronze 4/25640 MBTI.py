import sys; input=sys.stdin.readline

def main():
    mbti = input().rstrip()
    n = int(input())
    ans = 0
    for i in range(n):
        string = input().rstrip()
        if mbti == string:
            ans += 1
    print(ans)

if __name__=='__main__':
    main()
