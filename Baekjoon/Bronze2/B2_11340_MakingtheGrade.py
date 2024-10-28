import sys
import math
input = sys.stdin.readline

def main():
    num_cases = int(input().strip())
    results = []
    
    for _ in range(num_cases):
        a, b, c = map(int, input().strip().split())
        
        total_weighted_score = a * 15 + b * 20 + c * 25
        
        if total_weighted_score < 5000:
            results.append("impossible")
        else:
            min_final_score = math.ceil((9000 - total_weighted_score) / 40.0)
            results.append(min_final_score)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
