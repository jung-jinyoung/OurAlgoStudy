from collections import deque
import sys
input = sys.stdin.readline

def dfs(now,visit,cnt):
    if cnt == 5:
        print(1)
        exit()
    for nxt in graph[now]:
        if not visit[nxt]:
            visit[nxt] = 1
            dfs(nxt,visit,cnt+1)
            visit[nxt] = 0

n, m = map(int, input().split()) # 사람수, 간선 수
graph = [[] for _ in range(n)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for node in range(n):
    visit = [ 0 for _ in range(n)]
    visit[node] = 1 # 첫방문 노드는 visit 1
    dfs(node,visit,1) #노드마다 visit 따로 계산,방문노드 갯수
print(0)
