import sys
input = sys.stdin.readline

def main():
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    T = int(input())
    for _ in range(T):
        n, c = map(str, input().split())
        k = alpha.index(c)
        for i in range(1, int(n)+1):
            if k > 25:
                k -= 26
            print(alpha[k] * i)
            k += 1
        print()

if __name__ == '__main__':
    main()
