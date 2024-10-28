import sys
from collections import deque

input = sys.stdin.readline

if __name__ == '__main__':
    dxy = ((1, 0), (0, 1), (-1, 0), (0, -1))

    R, C = map(int, input().split())
    maps = [[] for _ in range(R)]

    whites = []
    deq = deque()
    temp_deq = deque()
    water_deq = deque()
    temp_water_deq = deque()

    visited = [[False] * C for _ in range(R)]
    water_visited = [[False] * C for _ in range(R)]

    cnt = 1
    for i in range(R):
        string = input().rstrip()
        for j in range(C):
            if string[j] == '.':
                water_visited[i][j] = True
                water_deq.append((i, j))
                maps[i].append(0)
            elif string[j] == 'X':
                maps[i].append(-1)
            elif string[j] == 'L':
                if cnt == 1:
                    # maps[i].append(1)
                    maps[i].append(0)
                    cnt += 1
                else:
                    # maps[i].append(2)
                    maps[i].append(0)
                whites.append((i, j))
                water_deq.append((i, j))

    x1, y1, x2, y2 = whites[0][0], whites[0][1], whites[1][0], whites[1][1]
    deq.append((x1, y1))
    visited[x1][y1] = True
    ans = 0


    def melt():
        while water_deq:
            x, y = water_deq.popleft()
            if maps[x][y] == -1:
                maps[x][y] = 0
            for dx, dy in dxy:
                nx, ny = x + dx, y + dy
                if 0 <= nx < R and 0 <= ny < C and not water_visited[nx][ny]:
                    if maps[nx][ny] == -1:
                        temp_water_deq.append((nx, ny))
                    else:
                        water_deq.append((nx, ny))
                    water_visited[nx][ny] = True


    def solve():
        while deq:
            x, y = deq.popleft()
            if x == x2 and y == y2:
                return True
            for dx, dy in dxy:
                nx, ny = x + dx, y + dy
                if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny]:
                    if maps[nx][ny] == 0:
                        deq.append((nx, ny))
                    else:
                        temp_deq.append((nx, ny))
                    visited[nx][ny] = True
        return False


    while True:
        melt()
        if solve():
            print(ans)
            break
        deq = temp_deq
        temp_deq = deque()
        water_deq = temp_water_deq
        temp_water_deq = deque()
        ans += 1