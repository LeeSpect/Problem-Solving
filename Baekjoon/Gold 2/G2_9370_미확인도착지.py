# 121,432 KB / 296 ms
import sys
import heapq as hq
input = sys.stdin.readline

def solve(root):
    dists = [int(1e9) for _ in range(n+1)]
    dists[root] = 0
    heap = [(0, root)]
    while heap:
        dist, start = hq.heappop(heap)
        if dists[start] < dist: continue
        
        for next_node, wei in graph[start]:
            next_dist = dist + wei
            if dists[next_node] <= next_dist: continue
            hq.heappush(heap, (next_dist, next_node))
            dists[next_node] = next_dist
    
    return dists
    

T = int(input())
ans=''
for tc in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    
    graph = [[] for _ in range(n+1)]
    
    h_to_g = 0
    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))
        if (a==h and b==g) or (a==g and b==h):
            h_to_g = d
    
    candidates = [int(input()) for _ in range(t)]
    
    dist_s = solve(s)
    if dist_s[g] > dist_s[h]:
        next_start = g
    else:
        next_start = h
    
    dist_n = solve(next_start)

    ret = []
    for candidate in candidates:
        # if dist_s[candidate]==int(1e9): continue
        # if ((dist_s[candidate] == dist_s[h] + h_to_g + dist_g[candidate]) or 
            # (dist_s[candidate] == dist_s[g] + h_to_g + dist_h[candidate])):
            # ret.append(candidate)
        if dist_s[next_start] + dist_n[candidate] == dist_s[candidate]:
            ret.append(candidate)
    # print(*sorted(ret))
    ans+=' '.join(list(map(str,sorted(ret))))+"\n"
print(ans)
                


# 틀린 코드
        
# candidates에 있으면, candidates에서 제거하고 candidates_visited에 넣는다.
# candidates_visited에 이씅면 continue
    # 후보에 도착했는데, isOK가 0이라면, 해당 후보는 절대 목적지가 될 수 없다. visited에 그냥 넣는다.
    # 후보에 도착했는데, isOK가 -1이면, ans에 넣는다.
# T = int(input())
# ans=''
# for tc in range(T):
#     n, m, t = map(int, input().split())
#     s, g, h = map(int, input().split())
    
#     graph = [[] for _ in range(n+1)]
#     dists = [int(1e9) for _ in range(n+1)]

#     for _ in range(m):
#         a, b, d = map(int, input().split())
#         graph[a].append((b, d))
#         graph[b].append((a, d))
    
#     candidates = set(int(input()) for _ in range(t))
#     candidates_visited = set()
#     ret = []
    
#     dists[s] = 0
#     # dist, isOK(-1:OK, 0:NO), start
#     heap = [(0, 0, s)]
#     while heap:
#         dist, isOK, start = hq.heappop(heap)
#         if dist >= dists[start]: continue
        
#         for next_node, wei in graph[start]:
#             next_dist = dist + wei
#             if dists[next_node] <= next_dist or next_node in candidates_visited:
#                 continue
            
#             # g에서 h로 가는 경로일 때
#             if (start==g and next_node==h) or (start==h and next_node==g):
#                 hq.heappush(heap, (next_dist, -1, next_node))
#                 dists[next_node] = next_dist
#             elif next_node in candidates:
#                 candidates.discard(next_node)
#                 candidates_visited.add(next_node)
#                 if isOK:
#                     ret.append(str(next_node))
#             else:
#                 hq.heappush(heap, (next_dist, isOK, next_node))
#                 dists[next_node] = next_dist

#     ans+=' '.join(sorted(ret))+"\n"
# print(ans)