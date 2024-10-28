def main():
    n = int(input())
    for i in range(n):
        a, b = map(int, input().split())
        ans = a * b
        if a > 1:
            ans -= 2*(a-1)
        print(a, b)
        print(ans)

if __name__=='__main__':
    main()
