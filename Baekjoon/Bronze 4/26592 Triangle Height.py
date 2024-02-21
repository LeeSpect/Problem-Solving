import sys; input = sys.stdin.readline

def main():
    T = int(input())
    for _ in range(T):
        a, b = map(float, input().split())
        h = a * 2 / b
        print(f'The height of the triangle is {h:.2f} units')

if __name__ == '__main__':
    main()
