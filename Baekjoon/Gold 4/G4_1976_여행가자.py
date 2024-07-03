import sys
from collections import deque

input = sys.stdin.readline

# 인접 행렬, 시작 노드, 방문 여부 리스트
def bfs(adjacency_matrix, start_node, visited):
    queue = deque([start_node])  # 큐 초기화 및 시작 노드를 큐에 추가
    visited[start_node] = True
    
    while queue:
        current_node = queue.popleft()

        # 현재 노드에 연결된 모든 이웃 노드를 탐색
        for neighbor, is_connected in enumerate(adjacency_matrix[current_node]): # 인덱스와 값을 함께 반환
            if is_connected and not visited[neighbor]:  # 이웃 노드가 연결되어 있고 방문하지 않았다면
                visited[neighbor] = True  # 이웃 노드를 방문한 것으로 표시
                queue.append(neighbor)  # 이웃 노드를 큐에 추가

num_cities = int(input().strip())
num_paths = int(input().strip())

adjacency_matrix = [list(map(int, input().split())) for _ in range(num_cities)]
visited = [False] * num_cities

travel_plan = list(map(int, input().split()))
# 시작 도시 설정 (입력된 도시는 1부터 시작하므로 0부터 시작하도록 조정)
start_city = travel_plan[0] - 1

bfs(adjacency_matrix, start_city, visited)

# 모든 여행 경로에 대해 방문 가능 여부 확인
can_travel = all(visited[city - 1] for city in travel_plan) # all: 모든 요소가 참이면 참 반환

print('YES' if can_travel else 'NO')
