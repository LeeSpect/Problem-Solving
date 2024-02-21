import sys; input = sys.stdin.readline

def main():
    n = int(input())
    l = list(map(int, input().split()))
    ans = 0
    for i in l:
        if i < n:
            ans += i
        else:
            ans += n
    print(ans)

if __name__ == '__main__':
    main()
