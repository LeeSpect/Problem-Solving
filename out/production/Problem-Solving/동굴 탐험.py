def dfs(node):
    stack = [node]
    visited[node] = True
    
    while stack:
        now = stack.pop() # 현재 노드
        for next in graph[now]: # 현재 노드와 연결된 다음 노드 - next
            if post_visited[now]:            # 현재 노드의 후행 노드가 있다면
                dfs(post_visited[now])       # 후행 노드로 이동
            if not visited[pre_visited[now]]:          # 선행 노드를 방문하지 않았다면
                post_visited[pre_visited[now]] = now   # 현재 노드를 후행 노드로 설정
                continue
            if not visited[next]:    # 방문하지 않은 노드면 스택에 추가
                stack.append(next)
                visited[next] = True # 방문 처리


def solution(n, path, order):
    global graph, pre_visited, post_visited, visited
    graph = [[] for _ in range(n)]
    pre_visited = [0] * n  # 선행 노드
    post_visited = [0] * n # 후행 노드
    visited = [False] * n  # 방문 여부
    
    for p in path:  # 양방향 그래프 생성
        graph[p[0]].append(p[1])
        graph[p[1]].append(p[0])
    
    for o in order:  # 선행, 후행 노드 설정
        pre_visited[o[1]] = o[0]
    
    dfs(0)
    
    if sum(visited) == n:  # 모든 노드를 방문했다면
        return True
    
    return False