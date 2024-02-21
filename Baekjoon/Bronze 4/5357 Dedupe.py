import sys; input = sys.stdin.readline

def main():
    n = int(input())
    for i in range(n):
        string = input().rstrip()
        ans = ''
        for c in string:
            if ans == '' or ans[-1] != c:
                ans += c
        print(ans)

if __name__=='__main__':
    main()
