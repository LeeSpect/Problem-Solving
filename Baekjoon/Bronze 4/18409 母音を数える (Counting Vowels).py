import sys; input=sys.stdin.readline

def main():
    n=int(input())
    string=input().rstrip()
    ans=0
    for i in range(n):
        if string[i] in 'aiueo':
            ans+=1
    print(ans)

if __name__=='__main__':
    main()
