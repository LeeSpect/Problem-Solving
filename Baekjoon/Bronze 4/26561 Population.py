import sys; input = sys.stdin.readline

def main():
    T = int(input())
    for i in range(T):
        p, t = map(int, input().split())
        p += t//4
        p -= t//7
        print(p)

if __name__ == '__main__':
    main()
