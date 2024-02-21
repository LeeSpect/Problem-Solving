import sys; input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    if n > 7:
        print(n - 7)
    else:
        print(m + 7)

if __name__ == '__main__':
    main()
