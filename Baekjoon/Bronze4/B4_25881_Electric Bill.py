import sys; input = sys.stdin.readline

def main():
    r, c = map(int, input().split())
    t = int(input())
    for i in range(t):
        k = int(input())
        if k > 1000:
            ans = (k-1000)*int(c) + int(r)*1000
        else:
            ans = r * k
        print(f'{k} {ans}')

if __name__=='__main__':
    main()
