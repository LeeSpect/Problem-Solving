import sys
from collections import deque
input = sys.stdin.readline

class Fish:
    def __init__(self, x, y, dir):
        self.x = x
        self.y = y
        self.dir = dir

def main():
    global shark_cor, final_route
    dxy=((0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1))
    shark_dxy=((-1,0),(0,-1),(1,0),(0,1))

    M, S = map(int, input().split())
    maps = [[list() for _ in range(4)] for _ in range(4)]
    fish_smell = [[0]*4 for _ in range(4)]

    for _ in range(M):
        fx, fy, d = map(int, input().split())
        fx -= 1
        fy -= 1
        maps[fx][fy].append(Fish(fx, fy, d-1))
        # fish_memo.append((fx, fy, d))
    sx, sy = map(int, input().split())
    shark_cor = (sx-1, sy-1)

    fish_memo = []

    def fish_move(maps):
        new_maps = [[list() for _ in range(4)] for _ in range(4)]
        for i in range(4):
            for j in range(4):
                for e in maps[i][j]:
                    if type(e) == Fish:
                        fish_memo.append((e.x, e.y, e.dir))   # fish_copy
                        nx, ny = e.x + dxy[e.dir][0], e.y + dxy[e.dir][1] # 방향 전환
                        temp_dir = e.dir # 빠져나오기 위함
                        is_no_way_to_go = False
                        while not (0<=nx<4 and 0<=ny<4 and fish_smell[nx][ny] == 0 and shark_cor!=(nx, ny)):
                            temp_dir = 7 if temp_dir==0 else temp_dir-1 # -1 되면 7로 바꿈
                            if temp_dir == e.dir: 
                                is_no_way_to_go = True
                                break         # 한바퀴 돌았는데 갈 곳 없으면 break
                            nx, ny = e.x + dxy[temp_dir][0], e.y + dxy[temp_dir][1]
                        if is_no_way_to_go: nx, ny = e.x, e.y # 방향 그대로면
                        new_maps[nx][ny].append(Fish(nx, ny, temp_dir))
        return new_maps
    

    def dfs(x, y, level, visited: set, route: str, score):
        global shark_cor, final_route, final_score
        # print(x, y, score, 'level:',level,'score:',score,'route:',route)
        if level == 3:
            if score > final_score:
                final_score = score
                final_route = route
            return
        for d in range(4):
            nx, ny = x+shark_dxy[d][0], y+shark_dxy[d][1]
            if 0<=nx<4 and 0<=ny<4:
                if (nx,ny) not in visited:
                    visited.add((nx, ny))
                    dfs(nx, ny, level+1, visited, route+str(d), score+len(new_maps[nx][ny]))
                    visited.discard((nx,ny))
                else:
                    dfs(nx, ny, level+1, visited, route+str(d), score)

    def shark_move():
        global shark_cor, final_route, final_score
        final_score = -1
        visited = set()
        route = ''
        dfs(shark_cor[0], shark_cor[1], 0, visited, route, 0)


    def del_fish(new_maps: list, final_route, fish_smell: list):
        nx, ny = shark_cor[0], shark_cor[1]
        for d in final_route:
            dir = int(d)
            # print(dir)
            nx += shark_dxy[dir][0]
            ny += shark_dxy[dir][1]
            if new_maps[nx][ny]:
                fish_smell[nx][ny] = 3  # 다음 과정에서 하나씩 지워줄 것이기 때문에 3으로
            new_maps[nx][ny].clear()
        return nx, ny
            
    def del_fish_smell(fish_smell):
        for i in range(4):
            for j in range(4):
                if fish_smell[i][j]:
                    fish_smell[i][j]-=1
    
    def add_fish(maps, new_maps):
        # print('maps')
        # for m in maps: print(m)
        for i in range(4):
            for j in range(4):
                if maps[i][j]:
                    for fish in maps[i][j]:
                        new_maps[i][j].append(fish)
                    
    def check_fish(maps):
        cnt = 0
        for i in range(4):
            for j in range(4):
                cnt += len(maps[i][j])
        return cnt

    for _ in range(S):
        # print(_)
        # for m in maps: print(m)
        new_maps=fish_move(maps)
        # print('-after_fish_move-')
        # for m in new_maps: print(m)

        final_route = ''
        shark_move()
        # print(final_route)

        shark_cor = del_fish(new_maps, final_route, fish_smell)
        # print('shark_cor:', shark_cor)
        # print('-after_eat_fish-')
        # for m in new_maps: print(m)

        del_fish_smell(fish_smell)
        # print('-fish_smell-')
        # for m in fish_smell: print(m)

        add_fish(maps, new_maps)    
        # print('-after_add_fish-')

        maps = new_maps
        # for m in maps: print(m)
    
    print(check_fish(maps))


if __name__ == '__main__':
    main()




