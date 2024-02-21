import sys; input = sys.stdin.readline

def main():
    t = int(input())
    for i in range(t):
        a, b, c = map(float, input().split())
        print(f'${a * b * c:.2f}')

if __name__=='__main__':
    main()
