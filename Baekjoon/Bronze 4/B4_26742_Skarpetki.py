import sys; input = sys.stdin.readline

def main():
    string = input().rstrip()
    B, C = string.count('B'), string.count('C')
    print((B//2) + (C//2))

if __name__ == '__main__':
    main()
