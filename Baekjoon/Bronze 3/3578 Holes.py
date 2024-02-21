import sys
input = sys.stdin.readline

def main():
    n = int(input())
    if n <= 1:
        print(1 if n == 0 else 0)
    else:
        ans = ''
        ans += '4' * (n % 2)
        ans += '8' * (n // 2)
        print(ans)

if __name__ == '__main__':
    main()
