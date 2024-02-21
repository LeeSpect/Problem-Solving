import sys
input = sys.stdin.readline

def main():
    T, S = map(int, input().split())
    if S or T <= 11 or 16 < T:
        print(280)
    else:
        print(320)

if __name__ == '__main__':
    main()
