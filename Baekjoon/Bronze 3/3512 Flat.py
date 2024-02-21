import sys; input = sys.stdin.readline

def main():
    n, c = map(int, input().split())
    d = {}
    d['bathroom'] = 0
    d['kitchen'] = 0
    d['balcony'] = 0
    d['other'] = 0
    d['bedroom'] = 0
    ans = 0

    for i in range(n):
        a, t = map(str, input().split())
        d[t] += int(a)
        ans += int(a)
    print(ans)
    print(d["bedroom"])
    print(f'{c * (ans - d["balcony"]/2):0.6f}')

if __name__ == "__main__":
    main()
