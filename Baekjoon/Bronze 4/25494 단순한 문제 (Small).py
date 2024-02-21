import sys; input=sys.stdin.readline

def main():
    n = int(input())
    for i in range(n):
        a, b, c = map(int, input().split())
        ans = 0
        for x in range(1, a+1):
            for y in range(1, b+1):
                for z in range(1, c+1):
                    if x % y == y % z == z % x:
                        ans += 1
        print(ans)

if __name__ == '__main__':
    main()
