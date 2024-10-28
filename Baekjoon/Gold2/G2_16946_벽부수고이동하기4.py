import sys
from collections import deque, defaultdict
input = sys.stdin.readline

dxy = ((0,1),(0,-1),(1,0),(-1,0))

N, M = map(int, input().split())
# maps = [list(map(int, input().split())) for _ in range(N)]
maps = []
for i in range(N):
    string = input().rstrip()
    maps.append([])
    for j in range(M):
        maps[i].append(int(string[j]))
cor_data = defaultdict(tuple)

# outer_visited: list(boolean): 전체 순회할 때의 방문여부 확인 
outer_visited = [[False]*M for _ in range(N)]

# 1. 전체 순회
    # 0 만나면 bfs 순회
    # inner_visited를 set으로 선언
    # - 0이 있는 곳 돌면서 0의 갯수 넣고 
idx=0
for i in range(N):
    for j in range(M):
        # 벽이거나, outer_visited에서 방문된 상태라면 continue
        if maps[i][j]==1 or outer_visited[i][j]: continue
        deq = deque()
        inner_visited = set()
        deq.append((i, j))
        inner_visited.add((i, j))
        
        cnt = 1
        while deq:
            x, y = deq.popleft()
            for d in range(4):
                nx, ny = x + dxy[d][0], y + dxy[d][1]
                if not (0<=nx<N and 0<=ny<M and (nx,ny) not in inner_visited and not outer_visited[nx][ny]): continue
                if maps[nx][ny] == 1: continue
                deq.append((nx, ny))
                inner_visited.add((nx, ny))
                outer_visited[nx][ny] = True
                cnt += 1

        for pos in inner_visited:
            cor_data[pos] = (cnt, idx)
        idx += 1

ans = []
for i in range(N):
    ans.append([])
    for j in range(M):
        if not maps[i][j]:
            ans[i].append('0')
            continue
            
        inner_visited_ans = []
        cnt = 1
        for d in range(4):
            nx, ny = i + dxy[d][0], j + dxy[d][1]
            if not (0<=nx<N and 0<=ny<M and not maps[nx][ny]): continue
            if cor_data[(nx,ny)][1] in inner_visited_ans: continue
            inner_visited_ans.append(cor_data[(nx,ny)][1])
            cnt += cor_data[(nx,ny)][0]
        ans[i].append(str(cnt%10))
    
for i in range(N):
    print(''.join(ans[i]))
            
        