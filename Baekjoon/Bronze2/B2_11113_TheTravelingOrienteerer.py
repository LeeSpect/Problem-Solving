import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def main():
    n = int(input().strip())
    points = []
    for _ in range(n):
        x, y = map(float, input().strip().split())
        points.append((x, y))
    
    m = int(input().strip())
    results = []
    for _ in range(m):
        p = int(input().strip())
        route = list(map(int, input().strip().split()))
        total_distance = 0
        for i in range(1, p):
            prev_point = points[route[i - 1]]
            current_point = points[route[i]]
            total_distance += calculate_distance(prev_point[0], prev_point[1], current_point[0], current_point[1])
        
        results.append(round(total_distance))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
