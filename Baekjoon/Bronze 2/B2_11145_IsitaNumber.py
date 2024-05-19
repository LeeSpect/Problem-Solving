import sys
input = sys.stdin.readline

def is_valid_integer(s):
    s = s.strip()
    print(str(int(s)) if s.isdigit() else "invalid input")

def main():
    T = int(input())
    for _ in range(T):
        test_case = input()
        is_valid_integer(test_case)

if __name__ == "__main__":
    main()
