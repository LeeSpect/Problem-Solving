import heapq
import sys
input = sys.stdin.readline

def max_people_within_d(n, segments, d):
    # 각 사람의 집과 사무실 위치에서 작은 값과 큰 값을 사용하여 구간을 정의
    intervals = [(min(h, o), max(h, o)) for h, o in segments]
    
    # 끝점을 기준으로 구간을 정렬
    intervals.sort(key=lambda x: x[1])

    max_count = 0
    heap = []
    
    for start, end in intervals:
        # 현재 구간의 끝점에서 d 이내에 포함되는 구간을 찾음
        if end - start <= d:
            while heap and heap[0] < end - d:
                heapq.heappop(heap)
            heapq.heappush(heap, start)
            max_count = max(max_count, len(heap))
    
    return max_count

# 입력 처리
n = int(input().strip())
segments = [tuple(map(int, input().strip().split())) for _ in range(n)]
d = int(input().strip())

# 결과 출력
print(max_people_within_d(n, segments, d))
