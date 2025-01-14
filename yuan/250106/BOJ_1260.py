"""
dfs 개념 다시 잡기
모든 노드를 방문해야하는 경우임
 -> 중복 노드 일때 멈추는 것 x

갈수 있는 노드 기준으로 dfs 가 실행되며,
앞의 dfs 부터 진행되기 됨

def dfs(s,path,visit):
    for nxt in graph[s]:
        if not visit[nxt]:
            visit[nxt] = 1 # 방문처리
            path.append(nxt)
            dfs(nxt,path,visit)
            # visit[nxt] = 0 # 방문취소

싸이클이 있을 수 있기 떄문에 방문취소 하면 안됨 
"""

from collections import deque

n, v, s = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(v):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def dfs(s, path, visit):
    for nxt in graph[s]:
        if not visit[nxt]:
            visit[nxt] = 1  # 방문처리
            path.append(nxt)
            dfs(nxt, path, visit)
            # visit[nxt] = 0 # 방문취소


def bfs(s, q, visit, path):
    while q:
        now = q.popleft()
        for nxt in graph[now]:
            if not visit[nxt]:
                visit[nxt] = 1
                path.append(nxt)
                q.append(nxt)
    return path


for idx, i in enumerate(graph):
    if len(i) > 1:
        graph[idx] = sorted(i)

# 방문가능하면 작은 수부터 방문
visit = [0] * (n + 1)
visit[s] = 1  # 방문처리
path = []
path.append(s)
dfs(s, path, visit)
print(*path)

visit = [0] * (n + 1)
visit[s] = 1  # 방문처리
path = []
path.append(s)
q = deque([s])
res_bfs = bfs(s, q, visit, path)
print(*res_bfs)
