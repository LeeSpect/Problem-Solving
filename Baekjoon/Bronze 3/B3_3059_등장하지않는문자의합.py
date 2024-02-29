import sys; input=sys.stdin.readline

def main():
    n = int(input())
    for i in range(n):
        string = input().rstrip()
        ans = 2015
        for e in string:
            ans -= ord(e)
        print(ans)

if __name__=='__main__':
    main()
