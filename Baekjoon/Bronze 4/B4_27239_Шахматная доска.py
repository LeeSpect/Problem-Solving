import sys; input = sys.stdin.readline

def main():
    n = int(input())
    alpha = 'abcdefgh'

    column = alpha[(n-1) % 8]
    raw = str((n + 7) // 8)

    print(column + raw)

if __name__ == '__main__':
    main()
