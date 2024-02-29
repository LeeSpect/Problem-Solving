import sys; input = sys.stdin.readline

def main():
    a, b = map(int, input().split())
    acre = a * b
    print((acre + (4840 * 5 - 1)) // (4840 * 5))

if __name__ == '__main__':
    main()
