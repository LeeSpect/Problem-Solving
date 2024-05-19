import sys
input = sys.stdin.readline

def binary_to_decimal():
    n = int(input().strip())
    
    results = []
    for _ in range(n):
        binary_string = input().strip()
        decimal_value = int(binary_string, 2)
        results.append(decimal_value)
    
    for result in results:
        print(result)

binary_to_decimal()
