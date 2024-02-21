import sys; input=sys.stdin.readline

def main():
    T = int(input())
    for _ in range(T):
        a, b = map(str, input().split())
        if b == 'kg':
            print(f'{float(a) * 2.2046:0.4f} lb')
        elif b == 'lb':
            print(f'{float(a) * 0.4536:0.4f} kg')
        elif b == 'l':
            print(f'{float(a) * 0.2642:0.4f} g')
        else:
            print(f'{float(a) * 3.7854:0.4f} l')

if __name__ == "__main__":
    main()
