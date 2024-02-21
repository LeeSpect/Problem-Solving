import sys; input = sys.stdin.readline

def main():
    x = int(input())
    y = int(input())
    for i in range(x, y+1, 60):
        print(f'All positions change in year {i}')

if __name__ == '__main__':
    main()
