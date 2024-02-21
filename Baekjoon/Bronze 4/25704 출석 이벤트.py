import sys; input = sys.stdin.readline

def main():
    n = int(input())
    p = int(input())
    if n < 5:
        print(p)
    elif n < 10:
        print(0 if p - 500 < 0 else p - 500)
    elif n < 15:
        a = min(p - 500, int(p * 0.9))
        print(0 if a < 0 else a)
    elif n < 20:
        a = min(p - 2000, int(p * 0.9))
        print(0 if a < 0 else a)
    else:
        a = min(p - 2000, int(p * 0.75))
        print(0 if a < 0 else a)

if __name__ == "__main__":
    main()
