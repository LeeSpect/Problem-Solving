# 틀린 코드
import sys; input = sys.stdin.readline

def main():
    n = int(input())
    print('int a;')
    print('int *ptr = &a;')
    for i in range(2, n+1):
        point = '*' * i
        print(f'int {point}ptr{i} = &ptr{i-1};')

if __name__ == "__main__":
    main()
    
# ------------------------------------------------------------------------------------------
# 수정 코드
import sys; input = sys.stdin.readline

def main():
    n = int(input())
    print('int a;')
    print('int *ptr = &a;')
    if n >= 2:
        print('int **ptr2 = &ptr;')
    for i in range(3, n+1):
        point = '*' * i
        print(f'int {point}ptr{i} = &ptr{i-1};')

if __name__ == "__main__":
    main()
